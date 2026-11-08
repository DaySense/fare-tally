# Reporting and ledger

In the user's language, lead with: lowest verified eligible airfare, practical low-fare alternative, meaningful cost/time/bag tradeoffs and unresolved constraints. Put accepted soft exceptions separately. Never call a hard deadline violation eligible.

Shortlist columns: option; currency/total/party basis; local outbound and full return arrival; hotel nights; bag allowance; journey/connection/ground costs; evidence level and checked timestamp. For finalists give every leg's airports, flight IDs, local dates/times, transfers, protection and fare/bags. Unknown flight numbers stay unknown.

Compare ticket/tax, required baggage/fees, transport/parking, extra transit lodging and hotel differences separately. Avoid double counting included benefits or shared transfers. Preserve original currency and dated FX assumptions. Unknown costs prevent a claim of lowest **total** cost. Different hotel dates/cities mean a saved night alone does not establish a saving.

## Ledger shape

A list, or an object with an `entries` list. Each entry uses a case ID copied from the plan, current `revision` and `status`. Actual observations/attempts need timezone-aware `checked_at` and `source`; an initial `planned` row may omit them. A `checked_final` entry also needs numeric nonnegative `amount`, three-letter `currency`, `party_basis` (`per_person` or `entire_party`) and `evidence_level` (`final_itinerary_list` or `prepayment_total`). Add sanitized URL, selected flights, account/coupon eligibility, bags, actual arrivals, reservation nights, constraint assessment, cost unknowns and private evidence location as needed.

Statuses: `planned`, `stage_price`, `checked_final`, `no_results`, `infeasible`, `loading_failed`, `blocked`, `skipped`. Only validated final/no-results/infeasible observations resolve a query. `infeasible` also needs `reason`; use it only after relevant result alternatives have been checked, not just the cheapest late flight. The helper checks structure, not truth or market completeness.

Coverage report: approved airports/date endpoints/families; constraint revision; resolved and pending counts; failures; unexamined timing/carrier/fare-bundle checks. Use “lowest verified within the searched scope.” If interrupted, save plan, ledger and next cases. Preserve earlier reports and label historical prices. Do not publish real traveler data to this open-source repository.

Keep query completion and traveler eligibility separate: a final observation can resolve a query while its cabin, required bag allowance or surface transfer remains unverified. Label such candidates conditional. For open jaws, keep a separate list of approved surface departure dates and unresolved arrival times/costs; the flight-query matrix does not enumerate those ground dates.
