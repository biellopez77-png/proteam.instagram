import { describe, expect, it, vi } from "vitest";
const calls: string[] = [];
let admin = false;
vi.mock("@tanstack/react-start", () => ({ createServerFn: () => { const b: any = { middleware: () => b, handler: (fn: any) => (ctx: any) => fn(ctx) }; return b; } }));
vi.mock("@/integrations/supabase/auth-middleware", () => ({ requireSupabaseAuth: {} }));
vi.mock("@/integrations/supabase/client.server", () => {
  const q: any = { select: () => q, eq: () => q, range: () => { calls.push("table"); return Promise.resolve({ data: [], error: null }); } };
  return { supabaseAdmin: { auth: { admin: { listUsers: () => { calls.push("listUsers"); return Promise.resolve({ data: { users: [{ id: "u1", email: "a@b.c", created_at: "2026-11-01T00:00:00Z", last_sign_in_at: null }] }, error: null }); } } }, from: () => q } };
});
import { getPlatformAnalytics } from "./admin-analytics.functions";
const ctx = { context: { userId: "x", supabase: { rpc: async () => ({ data: admin }) } } };
describe("getPlatformAnalytics", () => {
  it("rechaza a un no admin sin leer nada", async () => {
    admin = false; calls.length = 0;
    await expect((getPlatformAnalytics as any)(ctx)).rejects.toThrow("Accés denegat.");
    expect(calls).toEqual([]);
  });
  it("devuelve datos al admin", async () => {
    admin = true; calls.length = 0;
    const r = await (getPlatformAnalytics as any)(ctx);
    expect(r.accounts).toHaveLength(1); expect(r.accounts[0].billing).toBe("none"); expect(calls[0]).toBe("listUsers");
  });
});
