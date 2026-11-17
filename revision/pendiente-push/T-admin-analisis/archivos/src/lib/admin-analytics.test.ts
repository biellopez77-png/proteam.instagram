import { describe, expect, it } from "vitest";
import { bestBilling, filterAccounts, isActiveAccount, organizationBilling, rangeFromShortcut, signupSeries, summarize, weekStart, type AnalyticsAccount } from "./admin-analytics";

const NOW = Date.parse("2026-11-17T12:00:00Z");
const org = "o1";

describe("organizationBilling", () => {
  it("classifies the billing states that exist in the database", () => {
    expect(organizationBilling({ organization_id: org, billing_source: "trial", subscription_status: "trialing" }, [], NOW)).toBe("trial");
    expect(organizationBilling({ organization_id: org, billing_source: "manual", subscription_status: "manual_active" }, [], NOW)).toBe("promo");
    expect(organizationBilling({ organization_id: org, billing_source: "none", subscription_status: "expired" }, [], NOW)).toBe("none");
    expect(organizationBilling({ organization_id: org, billing_source: "stripe", subscription_status: "active", stripe_subscription_id: "sub_1" }, [], NOW)).toBe("paying");
    expect(organizationBilling(null, [], NOW)).toBe("none");
  });
  it("counts an active activation-code grant as promo, but not an expired one", () => {
    const base = { organization_id: org, source: "manual_code", status: "active" };
    expect(organizationBilling(null, [{ ...base, ends_at: "2027-01-01T00:00:00Z" }], NOW)).toBe("promo");
    expect(organizationBilling(null, [{ ...base, ends_at: "2026-01-01T00:00:00Z" }], NOW)).toBe("none");
  });
  it("a cancelled Stripe subscription is not paying", () => {
    expect(organizationBilling({ organization_id: org, billing_source: "stripe", subscription_status: "canceled", stripe_subscription_id: "sub_1" }, [], NOW)).toBe("none");
  });
});

describe("accounts", () => {
  const acc = (id: string, createdAt: string, billing: AnalyticsAccount["billing"], lastSignInAt: string | null = null): AnalyticsAccount => ({ id, name: id, email: null, createdAt, lastSignInAt, billing });
  const all = [acc("a", "2026-11-01T10:00:00Z", "trial", "2026-11-16T10:00:00Z"), acc("b", "2026-11-10T10:00:00Z", "promo", "2026-09-01T10:00:00Z"), acc("c", "2026-11-17T08:00:00Z", "none")];

  it("best billing wins across clubs", () => {
    expect(bestBilling(["none", "trial", "promo"])).toBe("promo");
    expect(bestBilling([])).toBe("none");
  });
  it("active means signed in within the last 30 days", () => {
    expect(all.map((a) => isActiveAccount(a, NOW))).toEqual([true, false, false]);
  });
  it("filters by billing and inclusive dates", () => {
    expect(filterAccounts(all, { billing: "all", from: "2026-11-10", to: "2026-11-17" }).map((a) => a.id)).toEqual(["b", "c"]);
    expect(filterAccounts(all, { billing: "trial", from: null, to: null }).map((a) => a.id)).toEqual(["a"]);
  });
  it("summarizes counts", () => {
    expect(summarize(all, [{ createdAt: "2026-11-02T00:00:00Z" }], NOW)).toEqual({ registered: 3, active: 1, waitlist: 1, byBilling: { paying: 0, promo: 1, trial: 1, none: 1 } });
  });
  it("builds a daily series with empty days", () => {
    const s = signupSeries(all, [{ createdAt: "2026-11-02T00:00:00Z" }], "2026-11-01", "2026-11-03");
    expect(s.unit).toBe("day");
    expect(s.points).toEqual([{ bucket: "2026-11-01", accounts: 1, waitlist: 0 }, { bucket: "2026-11-02", accounts: 0, waitlist: 1 }, { bucket: "2026-11-03", accounts: 0, waitlist: 0 }]);
  });
  it("switches to weeks for long ranges", () => {
    const s = signupSeries(all, [], "2026-08-01", "2026-11-17");
    expect(s.unit).toBe("week");
    expect(s.points[0]!.bucket).toBe(weekStart("2026-08-01"));
    expect(s.points.reduce((n, p) => n + p.accounts, 0)).toBe(3);
  });
  it("shortcuts", () => {
    expect(rangeFromShortcut(7, "2026-11-17")).toEqual({ from: "2026-11-11", to: "2026-11-17" });
    expect(rangeFromShortcut(null, "2026-11-17")).toEqual({ from: null, to: null });
    expect(weekStart("2026-11-17")).toBe("2026-11-16");
  });
});
