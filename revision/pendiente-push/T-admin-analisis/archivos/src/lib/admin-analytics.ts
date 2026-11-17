/**
 * Platform-admin analytics: pure helpers shared by the server function and the
 * «Anàlisi» tab. Only accounts with their own login are counted (auth users);
 * players without access never appear here.
 */

export type BillingCategory = "paying" | "promo" | "trial" | "none";
export type BillingFilter = "all" | BillingCategory;

export const BILLING_CATEGORIES: BillingCategory[] = ["paying", "promo", "trial", "none"];

/** Days without signing in after which an account no longer counts as active. */
export const ACTIVE_DAYS = 30;

export type AnalyticsAccount = {
  id: string;
  name: string;
  email: string | null;
  createdAt: string;
  lastSignInAt: string | null;
  billing: BillingCategory;
};

export type AnalyticsWaitlistEntry = { createdAt: string };

export type AnalyticsData = {
  generatedAt: string;
  accounts: AnalyticsAccount[];
  waitlist: AnalyticsWaitlistEntry[];
};

export type BillingRow = {
  organization_id: string;
  billing_source: string | null;
  subscription_status: string | null;
  stripe_subscription_id?: string | null;
};

export type GrantRow = {
  organization_id: string;
  source: string | null;
  status: string | null;
  ends_at: string | null;
};

const PAYING_STATUSES = new Set(["active", "past_due"]);
const RANK: Record<BillingCategory, number> = { paying: 3, promo: 2, trial: 1, none: 0 };

/**
 * Billing state of one organization.
 * - paying: a Stripe subscription that is active or past due.
 * - promo: access given with a ProTeam activation code (billing_source «manual»
 *   or an active grant whose source is «manual_code»).
 * - trial: free trial in progress («trialing»).
 * - none: anything else (expired, cancelled, no billing row).
 */
export function organizationBilling(billing: BillingRow | null | undefined, grants: GrantRow[], now: number): BillingCategory {
  const status = billing?.subscription_status ?? null;
  if (billing && (billing.billing_source === "stripe" || billing.stripe_subscription_id) && status && PAYING_STATUSES.has(status)) return "paying";
  const promoGrant = grants.some((g) => g.source === "manual_code" && g.status === "active" && (!g.ends_at || Date.parse(g.ends_at) > now));
  if (billing?.billing_source === "manual" || status === "manual_active" || promoGrant) return "promo";
  if (status === "trialing") return "trial";
  return "none";
}

/** An account with several clubs gets the best state among them. */
export function bestBilling(categories: BillingCategory[]): BillingCategory {
  return categories.reduce<BillingCategory>((best, c) => (RANK[c] > RANK[best] ? c : best), "none");
}

export function isActiveAccount(account: Pick<AnalyticsAccount, "lastSignInAt">, now: number, days = ACTIVE_DAYS): boolean {
  if (!account.lastSignInAt) return false;
  return now - Date.parse(account.lastSignInAt) <= days * 86_400_000;
}

export type AnalyticsFilters = { billing: BillingFilter; from: string | null; to: string | null };

/** `from`/`to` are inclusive calendar days (YYYY-MM-DD, UTC). */
export function inRange(iso: string, from: string | null, to: string | null): boolean {
  const day = iso.slice(0, 10);
  if (from && day < from) return false;
  if (to && day > to) return false;
  return true;
}

export function filterAccounts(accounts: AnalyticsAccount[], filters: AnalyticsFilters): AnalyticsAccount[] {
  return accounts.filter((a) => (filters.billing === "all" || a.billing === filters.billing) && inRange(a.createdAt, filters.from, filters.to));
}

export function summarize(accounts: AnalyticsAccount[], waitlist: AnalyticsWaitlistEntry[], now: number) {
  const byBilling: Record<BillingCategory, number> = { paying: 0, promo: 0, trial: 0, none: 0 };
  for (const a of accounts) byBilling[a.billing] += 1;
  return {
    registered: accounts.length,
    active: accounts.filter((a) => isActiveAccount(a, now)).length,
    waitlist: waitlist.length,
    byBilling,
  };
}

function addDays(day: string, n: number): string {
  const d = new Date(`${day}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
}

/** Monday of the ISO week of `day`. */
export function weekStart(day: string): string {
  const d = new Date(`${day}T00:00:00Z`);
  const offset = (d.getUTCDay() + 6) % 7;
  return addDays(day, -offset);
}

export type SignupPoint = { bucket: string; accounts: number; waitlist: number };

/**
 * Sign-ups per day (ranges up to 62 days) or per week (longer ranges), with
 * empty buckets filled so the chart keeps a real time axis.
 */
export function signupSeries(accounts: { createdAt: string }[], waitlist: { createdAt: string }[], from: string | null, to: string | null): { unit: "day" | "week"; points: SignupPoint[] } {
  const days = [...accounts, ...waitlist].map((r) => r.createdAt.slice(0, 10)).sort();
  const start = from ?? days[0];
  const end = to ?? days[days.length - 1];
  if (!start || !end || start > end) return { unit: "day", points: [] };
  const span = Math.round((Date.parse(`${end}T00:00:00Z`) - Date.parse(`${start}T00:00:00Z`)) / 86_400_000) + 1;
  const unit: "day" | "week" = span > 62 ? "week" : "day";
  const key = (day: string) => (unit === "week" ? weekStart(day) : day);
  const map = new Map<string, SignupPoint>();
  for (let b = key(start); b <= end; b = addDays(b, unit === "week" ? 7 : 1)) map.set(b, { bucket: b, accounts: 0, waitlist: 0 });
  for (const a of accounts) { const p = map.get(key(a.createdAt.slice(0, 10))); if (p) p.accounts += 1; }
  for (const w of waitlist) { const p = map.get(key(w.createdAt.slice(0, 10))); if (p) p.waitlist += 1; }
  return { unit, points: [...map.values()] };
}

/** Shortcut ranges for the date filter; `null` days means «everything». */
export function rangeFromShortcut(days: number | null, today: string): { from: string | null; to: string | null } {
  if (days === null) return { from: null, to: null };
  return { from: addDays(today, -(days - 1)), to: today };
}
