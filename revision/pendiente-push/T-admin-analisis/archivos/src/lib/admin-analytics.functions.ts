import { createServerFn } from "@tanstack/react-start";
import { requireSupabaseAuth } from "@/integrations/supabase/auth-middleware";
import {
  bestBilling,
  organizationBilling,
  type AnalyticsAccount,
  type AnalyticsData,
  type AnalyticsWaitlistEntry,
  type BillingCategory,
  type BillingRow,
  type GrantRow,
} from "@/lib/admin-analytics";

const MAX_ROWS = 20_000;

/**
 * Platform-admin only, read-only: accounts with their own login, waitlist sign-ups
 * and billing state. Same admin check as the rest of /admin (`is_platform_admin`);
 * the service client is only used after that check and nothing is written.
 * Player data (players without an account, stats, health…) is never read.
 */
export const getPlatformAnalytics = createServerFn({ method: "GET" })
  .middleware([requireSupabaseAuth])
  .handler(async ({ context }): Promise<AnalyticsData> => {
    const { data: role } = await context.supabase.rpc("is_platform_admin", { _user_id: context.userId });
    if (role !== true) throw new Error("Accés denegat.");
    const { supabaseAdmin } = await import("@/integrations/supabase/client.server");

    const users: { id: string; email?: string | null; created_at: string; last_sign_in_at?: string | null }[] = [];
    for (let page = 1; page <= 20; page++) {
      const { data, error } = await supabaseAdmin.auth.admin.listUsers({ page, perPage: 1000 });
      if (error) throw new Error("No s'han pogut carregar els comptes.");
      users.push(...data.users);
      if (data.users.length < 1000) break;
    }

    const [profiles, organizations, members, teams, billing, grants, leads] = await Promise.all([
      supabaseAdmin.from("profiles").select("id,display_name,name,surname,account_type").range(0, MAX_ROWS),
      supabaseAdmin.from("organizations").select("id,owner_user_id").range(0, MAX_ROWS),
      supabaseAdmin.from("team_members").select("user_id,team_id,status").eq("status", "active").range(0, MAX_ROWS),
      supabaseAdmin.from("teams").select("id,organization_id").range(0, MAX_ROWS),
      supabaseAdmin.from("organization_billing").select("organization_id,billing_source,subscription_status,stripe_subscription_id").range(0, MAX_ROWS),
      supabaseAdmin.from("organization_access_grants").select("organization_id,source,status,ends_at,note,created_at").range(0, MAX_ROWS),
      supabaseAdmin.from("leads").select("origen,source,created_at").range(0, MAX_ROWS),
    ]);
    for (const result of [profiles, organizations, members, teams, billing, grants, leads]) {
      if (result.error) throw new Error("No s'han pogut carregar les dades d'anàlisi.");
    }

    const now = Date.now();
    const grantRows = (grants.data ?? []) as unknown as (GrantRow & { note: string | null; created_at: string })[];
    const grantsByOrg = new Map<string, GrantRow[]>();
    for (const g of grantRows) grantsByOrg.set(g.organization_id, [...(grantsByOrg.get(g.organization_id) ?? []), g]);
    const orgBilling = new Map<string, BillingCategory>();
    const billingByOrg = new Map(((billing.data ?? []) as unknown as BillingRow[]).map((b) => [b.organization_id, b]));
    const orgIds = new Set([...((organizations.data ?? []) as unknown as { id: string }[]).map((o) => o.id), ...billingByOrg.keys()]);
    for (const id of orgIds) orgBilling.set(id, organizationBilling(billingByOrg.get(id), grantsByOrg.get(id) ?? [], now));

    const orgsByUser = new Map<string, Set<string>>();
    const link = (userId: string | null, orgId: string | null | undefined) => {
      if (!userId || !orgId) return;
      if (!orgsByUser.has(userId)) orgsByUser.set(userId, new Set());
      orgsByUser.get(userId)!.add(orgId);
    };
    for (const o of (organizations.data ?? []) as unknown as { id: string; owner_user_id: string | null }[]) link(o.owner_user_id, o.id);
    const teamOrg = new Map(((teams.data ?? []) as unknown as { id: string; organization_id: string }[]).map((t) => [t.id, t.organization_id]));
    for (const m of (members.data ?? []) as unknown as { user_id: string | null; team_id: string }[]) link(m.user_id, teamOrg.get(m.team_id));

    const profileById = new Map(((profiles.data ?? []) as unknown as { id: string; display_name: string | null; name: string | null; surname: string | null; account_type: string | null }[]).map((p) => [p.id, p]));
    const accounts: AnalyticsAccount[] = users
      .filter((u) => profileById.get(u.id)?.account_type !== "platform_administrator")
      .map((u) => {
        const p = profileById.get(u.id);
        const name = p?.display_name || [p?.name, p?.surname].filter(Boolean).join(" ") || "";
        const categories = [...(orgsByUser.get(u.id) ?? [])].map((id) => orgBilling.get(id) ?? "none");
        return { id: u.id, name, email: u.email ?? null, createdAt: u.created_at, lastSignInAt: u.last_sign_in_at ?? null, billing: bestBilling(categories) };
      })
      .sort((a, b) => b.createdAt.localeCompare(a.createdAt));

    // Waitlist: first clubs created during the Blackout Friday campaign (their
    // trial grant carries the waitlist note) plus public leads tagged as waitlist.
    const waitlist: AnalyticsWaitlistEntry[] = [
      ...grantRows.filter((g) => /^llista d.espera/i.test(g.note ?? "")).map((g) => ({ createdAt: g.created_at })),
      ...((leads.data ?? []) as unknown as { origen: string | null; source: string | null; created_at: string }[])
        .filter((l) => /espera|waitlist/i.test(`${l.origen ?? ""} ${l.source ?? ""}`))
        .map((l) => ({ createdAt: l.created_at })),
    ];

    return { generatedAt: new Date(now).toISOString(), accounts, waitlist };
  });
