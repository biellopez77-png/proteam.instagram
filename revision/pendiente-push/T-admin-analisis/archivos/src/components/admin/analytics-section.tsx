import { useMemo, useState, type ReactNode } from "react";
import { useQuery } from "@tanstack/react-query";
import { useServerFn } from "@tanstack/react-start";
import { Activity, Clock, CreditCard, ListChecks, Ticket, UserPlus, Users, UserX } from "lucide-react";
import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { getPlatformAnalytics } from "@/lib/admin-analytics.functions";
import { ACTIVE_DAYS, BILLING_CATEGORIES, filterAccounts, inRange, rangeFromShortcut, signupSeries, summarize, type BillingCategory, type BillingFilter } from "@/lib/admin-analytics";
import { localeForLang } from "@/lib/date-utils";
import { useI18n } from "@/lib/i18n";

const BILLING_LABELS: Record<BillingFilter, string> = {
  all: "Tots",
  paying: "Pagant",
  promo: "Amb codi promocional",
  trial: "En prova",
  none: "Sense pla",
};

const SHORTCUTS: { days: number | null; label: string }[] = [
  { days: 7, label: "7 dies" },
  { days: 30, label: "30 dies" },
  { days: null, label: "Tot" },
];

const TABLE_LIMIT = 50;
const tooltipStyle = { background: "var(--popover)", border: "1px solid var(--border)", borderRadius: 12, fontSize: 12, color: "var(--popover-foreground)" };
const tick = { fontSize: 10, fill: "var(--muted-foreground)" };
const field = "h-11 w-full rounded-lg border border-input bg-background px-3 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring";
const chip = (on: boolean) => `inline-flex min-h-11 items-center rounded-full border px-3 text-xs font-medium ${on ? "border-primary bg-primary text-primary-foreground" : "border-border bg-background text-foreground hover:bg-muted"}`;

function todayUTC() {
  return new Date().toISOString().slice(0, 10);
}

/** «Anàlisi» tab of /admin: accounts, waitlist and billing, filtered by state and sign-up date. */
export function AnalyticsSection() {
  const { t, lang } = useI18n();
  const locale = localeForLang(lang);
  const fetchAnalytics = useServerFn(getPlatformAnalytics);
  const query = useQuery({ queryKey: ["platform-analytics"], queryFn: () => fetchAnalytics(), staleTime: 60_000 });
  const [billing, setBilling] = useState<BillingFilter>("all");
  const [range, setRange] = useState<{ from: string | null; to: string | null }>({ from: null, to: null });
  const [shortcut, setShortcut] = useState<number | null | "custom">(null);

  const view = useMemo(() => {
    const data = query.data;
    if (!data) return null;
    const now = Date.parse(data.generatedAt);
    const accounts = filterAccounts(data.accounts, { billing, ...range });
    const waitlist = data.waitlist.filter((w) => inRange(w.createdAt, range.from, range.to));
    return { accounts, waitlist, summary: summarize(accounts, waitlist, now), series: signupSeries(accounts, waitlist, range.from, range.to) };
  }, [query.data, billing, range]);

  const pickShortcut = (days: number | null) => {
    setShortcut(days);
    setRange(rangeFromShortcut(days, todayUTC()));
  };
  const setDate = (key: "from" | "to", value: string) => {
    setShortcut("custom");
    setRange((r) => ({ ...r, [key]: value || null }));
  };
  const fmtDay = (day: string) => new Date(`${day}T12:00:00Z`).toLocaleDateString(locale, { day: "numeric", month: "short" }).replace(/\./g, "");

  if (query.isLoading) return <p className="rounded-lg border border-border bg-card p-4 text-sm text-muted-foreground">{t("Carregant l'anàlisi…")}</p>;
  if (query.isError || !view) return <p role="alert" className="rounded-lg border border-border bg-card p-4 text-sm text-destructive">{t("No s'ha pogut carregar l'anàlisi.")}</p>;

  const { summary, series } = view;
  return (
    <section className="space-y-4">
      <div className="space-y-3 rounded-lg border border-border bg-card p-4">
        <div>
          <p className="text-xs font-medium text-muted-foreground">{t("Facturació")}</p>
          <div className="mt-1 flex flex-wrap gap-2">
            {(["all", ...BILLING_CATEGORIES] as BillingFilter[]).map((key) => (
              <button key={key} type="button" aria-pressed={billing === key} className={chip(billing === key)} onClick={() => setBilling(key)}>{t(BILLING_LABELS[key])}</button>
            ))}
          </div>
        </div>
        <div className="grid gap-3 sm:grid-cols-[auto_1fr_1fr] sm:items-end">
          <div>
            <p className="text-xs font-medium text-muted-foreground">{t("Data d'alta")}</p>
            <div className="mt-1 flex flex-wrap gap-2">
              {SHORTCUTS.map((s) => (
                <button key={s.label} type="button" aria-pressed={shortcut === s.days} className={chip(shortcut === s.days)} onClick={() => pickShortcut(s.days)}>{t(s.label)}</button>
              ))}
            </div>
          </div>
          <label className="text-xs font-medium text-muted-foreground">{t("Des de")}
            <input type="date" className={`${field} mt-1`} value={range.from ?? ""} max={range.to ?? undefined} onChange={(e) => setDate("from", e.target.value)} />
          </label>
          <label className="text-xs font-medium text-muted-foreground">{t("Fins a")}
            <input type="date" className={`${field} mt-1`} value={range.to ?? ""} min={range.from ?? undefined} onChange={(e) => setDate("to", e.target.value)} />
          </label>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
        <StatCard icon={<Users className="size-4" />} label={t("Comptes registrats")} value={summary.registered} help={t("Persones amb compte propi i accés a ProTeam. No inclou jugadors sense accés.")} />
        <StatCard icon={<Activity className="size-4" />} label={t("Comptes actius")} value={summary.active} help={t("Han entrat a ProTeam en els últims {0} dies.", ACTIVE_DAYS)} />
        <StatCard icon={<ListChecks className="size-4" />} label={t("Llista d'espera")} value={summary.waitlist} help={t("Clubs creats durant la campanya Blackout Friday i inscripcions a la llista des de la web.")} />
        <StatCard icon={<UserPlus className="size-4" />} label={t("Altes al període")} value={summary.registered + summary.waitlist} help={t("Comptes i llista d'espera dins dels filtres.")} />
      </div>
      <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
        <StatCard icon={<CreditCard className="size-4" />} label={t(BILLING_LABELS.paying)} value={summary.byBilling.paying} help={t("Subscripció de Stripe activa.")} />
        <StatCard icon={<Ticket className="size-4" />} label={t(BILLING_LABELS.promo)} value={summary.byBilling.promo} help={t("Accés amb un codi d'activació de ProTeam.")} />
        <StatCard icon={<Clock className="size-4" />} label={t(BILLING_LABELS.trial)} value={summary.byBilling.trial} help={t("Prova gratuïta en curs.")} />
        <StatCard icon={<UserX className="size-4" />} label={t(BILLING_LABELS.none)} value={summary.byBilling.none} help={t("Sense club, prova acabada o subscripció cancel·lada.")} />
      </div>

      <div className="rounded-lg border border-border bg-card p-4">
        <h2 className="text-sm font-semibold">{series.unit === "week" ? t("Altes per setmana") : t("Altes per dia")}</h2>
        {series.points.length === 0 ? (
          <p className="mt-3 text-sm text-muted-foreground">{t("Cap alta en aquestes dates.")}</p>
        ) : (
          <div className="mt-3 h-56 min-w-0">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={series.points.map((p) => ({ ...p, label: fmtDay(p.bucket) }))} margin={{ top: 4, right: 0, left: -24, bottom: 0 }}>
                <CartesianGrid vertical={false} stroke="var(--border)" />
                <XAxis dataKey="label" tickLine={false} axisLine={false} tick={tick} interval="preserveStartEnd" minTickGap={16} />
                <YAxis allowDecimals={false} tickLine={false} axisLine={false} tick={tick} width={40} />
                <Tooltip cursor={{ fill: "var(--muted)" }} contentStyle={tooltipStyle} formatter={(v, n) => [String(v ?? 0), n === "accounts" ? t("Comptes") : t("Llista d'espera")]} />
                <Legend iconSize={8} wrapperStyle={{ fontSize: 11 }} formatter={(n) => (n === "accounts" ? t("Comptes") : t("Llista d'espera"))} />
                <Bar dataKey="accounts" fill="var(--primary)" radius={[4, 4, 0, 0]} />
                <Bar dataKey="waitlist" fill="var(--cyan)" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>

      <div className="rounded-lg border border-border bg-card p-4">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <h2 className="text-sm font-semibold">{t("Comptes filtrats")}</h2>
          <span className="text-xs text-muted-foreground">{t("Mostrant {0} de {1}", Math.min(TABLE_LIMIT, view.accounts.length), view.accounts.length)}</span>
        </div>
        {view.accounts.length === 0 ? (
          <p className="mt-3 text-sm text-muted-foreground">{t("Cap compte amb aquests filtres.")}</p>
        ) : (
          <div className="mt-3 overflow-x-auto">
            <table className="w-full min-w-[520px] text-left text-sm">
              <thead className="text-xs text-muted-foreground">
                <tr>
                  <th scope="col" className="py-2 pr-3 font-medium">{t("Nom")}</th>
                  <th scope="col" className="py-2 pr-3 font-medium">{t("Email")}</th>
                  <th scope="col" className="py-2 pr-3 font-medium">{t("Alta")}</th>
                  <th scope="col" className="py-2 font-medium">{t("Estat")}</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border">
                {view.accounts.slice(0, TABLE_LIMIT).map((a) => (
                  <tr key={a.id}>
                    <td className="max-w-40 truncate py-2 pr-3 font-medium" data-i18n-skip>{a.name || "—"}</td>
                    <td className="max-w-56 truncate py-2 pr-3 text-muted-foreground" data-i18n-skip>{a.email ?? "—"}</td>
                    <td className="whitespace-nowrap py-2 pr-3 tabular-nums">{new Date(a.createdAt).toLocaleDateString(locale)}</td>
                    <td className="py-2"><BillingBadge category={a.billing} label={t(BILLING_LABELS[a.billing])} /></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </section>
  );
}

function StatCard({ icon, label, value, help }: { icon: ReactNode; label: string; value: number; help: string }) {
  return (
    <div className="min-w-0 rounded-lg border border-border bg-card p-3">
      <p className="flex items-center gap-1.5 text-xs font-medium text-muted-foreground"><span className="text-primary" aria-hidden="true">{icon}</span><span className="truncate">{label}</span></p>
      <p className="mt-1 text-2xl font-semibold tabular-nums">{value}</p>
      <p className="mt-1 text-[11px] leading-snug text-muted-foreground">{help}</p>
    </div>
  );
}

function BillingBadge({ category, label }: { category: BillingCategory; label: string }) {
  const tone: Record<BillingCategory, string> = {
    paying: "bg-primary/15 text-primary",
    promo: "bg-secondary text-secondary-foreground",
    trial: "bg-muted text-foreground",
    none: "bg-muted text-muted-foreground",
  };
  return <span className={`inline-flex rounded-full px-2 py-0.5 text-xs font-medium ${tone[category]}`}>{label}</span>;
}
