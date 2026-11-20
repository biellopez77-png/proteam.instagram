import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:80])
    s = s.replace(old, new)

rep('import { enqueue, flushQueue, newId, pendingCount, undoOp, lastUndoableOp } from "@/lib/live-queue";',
    'import { enqueue, flushQueue, newId, pendingCount, readQueue, undoOp, lastUndoableOp } from "@/lib/live-queue";')

rep('  const [timeoutLeft, setTimeoutLeft] = useState<number | null>(null);\n',
    '  const [timeoutLeft, setTimeoutLeft] = useState<number | null>(null);\n'
    '  /** Wall-clock end of the running timeout: the countdown never drifts when the screen sleeps. */\n'
    '  const [timeoutEnd, setTimeoutEnd] = useState<number | null>(null);\n'
    '  const timeoutBusy = useRef(false);\n')

rep('''    setPending(pendingCount(id));
    setSyncError(res.failed > 0);
    if (res.sent > 0 || res.reverted > 0)
      await qc.invalidateQueries({ queryKey: ["live-match", id] });
  }, [id, addFn, revertFn, qc]);''',
'''    // Refetch first: queued actions keep counting (timeouts used) until the
    // server copy is on screen, so counters never dip for a moment.
    if (res.sent > 0 || res.reverted > 0)
      await qc.invalidateQueries({ queryKey: ["live-match", id] });
    setPending(pendingCount(id));
    setSyncError(res.failed > 0);
  }, [id, addFn, revertFn, qc]);''')

rep('''  // Timeout countdown (visual only: it never touches the match clock).
  useEffect(() => {
    if (timeoutLeft === null) return;
    if (timeoutLeft <= 0) {
      const t = setTimeout(() => setTimeoutLeft(null), 1500);
      return () => clearTimeout(t);
    }
    const i = setInterval(() => setTimeoutLeft((s) => (s === null ? null : s - 1)), 1000);
    return () => clearInterval(i);
  }, [timeoutLeft]);''',
'''  // Timeout countdown (visual only: it never touches the match clock).
  // Anchored to wall time like the match clock: a locked phone or a hidden
  // tab must not leave a minute-long timeout showing seconds that are gone.
  useEffect(() => {
    if (timeoutEnd === null) return;
    const tick = () => setTimeoutLeft(Math.max(0, Math.ceil((timeoutEnd - Date.now()) / 1000)));
    tick();
    const i = setInterval(tick, 500);
    document.addEventListener("visibilitychange", tick);
    window.addEventListener("focus", tick);
    return () => {
      clearInterval(i);
      document.removeEventListener("visibilitychange", tick);
      window.removeEventListener("focus", tick);
    };
  }, [timeoutEnd]);
  useEffect(() => {
    if (timeoutLeft !== 0) return;
    const t = setTimeout(() => {
      setTimeoutLeft(null);
      setTimeoutEnd(null);
    }, 1500);
    return () => clearTimeout(t);
  }, [timeoutLeft]);''')

rep('''  const timeoutsUsed = {
    us: events.filter((e) => e.type === "timeout_us").length,
    them: events.filter((e) => e.type === "timeout_them").length,
  };''',
'''  // Saved timeouts plus the ones still waiting in the offline queue: without
  // signal the button must not offer a timeout the team has already used.
  const timeoutsUsed = useMemo(() => {
    const used = {
      us: events.filter((e) => e.type === "timeout_us").length,
      them: events.filter((e) => e.type === "timeout_them").length,
    };
    const onServer = new Set(
      events.map((e) => (e as { client_id?: string | null }).client_id).filter(Boolean),
    );
    for (const op of readQueue(id)) {
      if (op.cancelled) continue;
      const evts = (op.payload as { events?: { client_id: string; type: string }[] } | null)?.events ?? [];
      for (const e of evts) {
        if (onServer.has(e.client_id)) continue;
        if (e.type === "timeout_us") used.us++;
        else if (e.type === "timeout_them") used.them++;
      }
    }
    return used;
    // `pending` changes whenever the local queue does.
  }, [events, id, pending]);''')

rep('''  async function recordTimeout(side: "us" | "them") {
    if (!guard()) return;
    const limit = side === "us" ? timeoutCfg.us : timeoutCfg.them;
    const used = side === "us" ? timeoutsUsed.us : timeoutsUsed.them;
    if (used >= limit) {
      toast.error(
        t(side === "us" ? "Tu equipo ya ha agotado los tiempos muertos ({0})." : "El rival ya ha agotado los tiempos muertos ({0}).", limit),
      );
      return;
    }
    const saved = await record([draft({ type: side === "us" ? "timeout_us" : "timeout_them", side })], {
      label: t(side === "us" ? "Tiempo muerto propio {0}/{1}" : "Tiempo muerto rival {0}/{1}", used + 1, limit),
    });
    if (saved && timeoutCfg.duration > 0) setTimeoutLeft(timeoutCfg.duration);
  }''',
'''  async function recordTimeout(side: "us" | "them") {
    if (!guard()) return;
    // A second tap while the first one is still pausing the clock would
    // record the same timeout twice.
    if (timeoutBusy.current) return;
    const limit = side === "us" ? timeoutCfg.us : timeoutCfg.them;
    const used = side === "us" ? timeoutsUsed.us : timeoutsUsed.them;
    if (used >= limit) {
      toast.error(
        t(side === "us" ? "Tu equipo ya ha agotado los tiempos muertos ({0})." : "El rival ya ha agotado los tiempos muertos ({0}).", limit),
      );
      return;
    }
    timeoutBusy.current = true;
    try {
      const saved = await record([draft({ type: side === "us" ? "timeout_us" : "timeout_them", side })], {
        label: t(side === "us" ? "Tiempo muerto propio {0}/{1}" : "Tiempo muerto rival {0}/{1}", used + 1, limit),
      });
      if (saved && timeoutCfg.duration > 0) setTimeoutEnd(Date.now() + timeoutCfg.duration * 1000);
    } finally {
      timeoutBusy.current = false;
    }
  }''')

rep('''                    className="rounded-lg border border-border py-1.5 text-[11px] font-semibold tracking-wide text-muted-foreground disabled:opacity-40"''',
'''                    className="min-h-11 rounded-lg border border-border py-1.5 text-[11px] font-semibold tracking-wide text-muted-foreground disabled:opacity-40"''')
open(p, "w", encoding="utf-8").write(s)
print("ok")
