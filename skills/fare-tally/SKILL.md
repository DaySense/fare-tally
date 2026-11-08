---
name: fare-tally
description: Find cheaper flights through a preference-led interview, flexible dates, nearby airports and verified total costs. Use for airfare research, return, multi-city and open-jaw comparisons. 帮助查找低价机票、灵活日期、周边机场和多程缺口程，并比较行李、时段与总成本。
---

# FareTally · 航价笔记

Find lower fares that fit this traveler. Respond in the user's language; support Chinese and English equally. This is research, not a booking service, flight-data API or guarantee of the absolute market minimum. Working browsing/search tools are required; the bundled script only plans and audits research.

## Agree on scope before fare searches

Read [the interview guide](references/intake.md). Reuse existing answers. Ask small relevant batches, not an exhaustive questionnaire.

Resolve material unknowns before fetching fares: route and approved airports, travel year/date windows, latest destination-local arrival, passengers/cabin/bags, budget-airline and transfer acceptance, and price versus convenience priorities. Ask about nearby airports at **both ends and intermediate cities**: more acceptable airports can expose cheaper fares, but extra ground cost/time can reverse the saving. Offer to identify airports if the traveler knows only cities. Do not add one without agreement.

Clarify **outbound date, outbound time, stay duration, return date and return time separately**. Translate “three days,” “after class,” “before 03:00” and conditional weekend preferences into explicit local dates/times, paid nights or usable days. Confirm city order, optional stops, open jaws and exceptions. Never inherit a previous traveler's identity, document status, dates or preferences.

Summarize hard constraints, soft preferences, exceptions, currency/party basis, sources and bounded coverage. Obtain acknowledgement before dependent fare searches when material choices remain unconfirmed. “Use these defaults and proceed” suffices; avoid repeating permission prompts for an agreed scope. While awaiting required answers, prepare the matrix. Disclose optional defaults; do not silently assume one adult, no bags or unlimited transfers.

## Tools and login

Use the requested platform when accessible. Ctrip is useful when requested, not universally cheapest. Do not assume Trip.com inventory, accounts or prices are identical. Offer suitable local platforms/airline-direct sources to English users rather than imposing a Chinese account.

If login is necessary, explain which site/browser, why, and what the user must do. Their browser login may not exist in yours. Have the user enter passwords, OTPs and CAPTCHA answers themselves; never request credentials or copy cookies. Verify visible account state before resuming. Usable anonymous fares may be compared if accepted and labeled separately from member/coupon prices.

If live access is unavailable or repeatedly blocked, explain the gap and offer a plan or labeled user-supplied quotes. Never invent a live fare or bypass access controls through hidden endpoints. Follow the host's supported tools and permissions.

## Plan coverage including earlier and later dates

Read [search and verification](references/search-and-evidence.md). List every approved route family, ordered leg, airport choice and **inclusive** date domain. Include all approved earlier/later dates, endpoints, return dates and stay combinations. Keep a baseline so the first cheap family does not consume all attention.

For nontrivial combinations use the offline helper and [its schema](references/coverage.md):

    python3 scripts/search_matrix.py plan examples/search-space.json --out /path/to/private-research/plan.json
    python3 scripts/search_matrix.py audit /path/to/private-research/plan.json /path/to/private-research/ledger.json

Resolve paths relative to this skill directory. The fictional example produces no prices. The helper enumerates candidate **departure-date queries**, not available flights or feasible hotel stays. Do not prune a later leg solely because its airport-local date is earlier: a date-line crossing can be chronologically valid. Establish flight and connection order from timezone-aware timestamps. Execute cases through supported site controls or an authorized documented API; never turn the matrix into guessed URL grids or undocumented scraping.

If Python is unavailable, maintain the same explicit matrix/ledger manually and disclose that the helper was not run.

If the matrix is large, disclose its size, narrow the agreed scope or complete explicit batches, and expose unsearched work. Do not silently sample center dates or discard expensive families. Check the day before/after each apparent winner within approved bounds, adjacent return dates, approved stay lengths and airport gaps. Ask before expanding outside approved dates.

Date coverage alone is not time/airline coverage. For finalists inspect practical early/daytime/evening alternatives and relevant carriers/baggage bundles. A modest domestic-flight premium may avoid a midnight arrival. Record unexamined alternatives. A teaser or sum of singles is not a valid lower bound for pruning a multi-city package.

## Verify complete itineraries and practical costs

Use whole multi-city/open-jaw pricing where supported; joint fares may differ from sums of singles. Split tickets are a separately verified alternative only if accepted, with baggage, protection and transit risks. Every leg/carrier/time/airport change requires repricing the **whole** selection.

Use the intended party, cabin/fare family, bags, currency and account conditions. If a source omits the requested cabin or required baggage allowance, label that candidate conditional; a carrier name or completed query audit does not prove those requirements. Distinguish teaser, selection-stage, final itinerary-list and safely viewable pre-payment totals. Do not enter passenger identity, create a hold, accept terms or pay merely to obtain a quote. Stop at the available evidence level if deeper verification requires a consequential action.

For finalists capture all local flight dates/times, airports/terminals when relevant, operating/marketing flights, stops, elapsed duration, layovers, airport changes, baggage handling and protection/self-transfer status. Missing flight numbers stay unknown. Check the **actual destination-local arrival date**, not just its clock time or departure day. Do not assume fixed UTC offsets across daylight-saving changes.

Calculate hotel nights from intended reservations. A 00:10 arrival may need the preceding night's room. A 01:00 departure may permit the preceding evening's checkout if accepted. Separate paid nights, usable days and early/late check-in assumptions. Apply weekend/conditional rules to actual local presence: a dawn Saturday departure is not automatically a usable Saturday.

Compare ticket, required bags, unavoidable fees, ground transfers and extra transit lodging without double counting. Unknown amounts stay unknown; the airfare winner is not automatically the total-cost winner. Hotel dates/cities can change rates, so “one fewer night” alone does not establish a saving.

For international transfers, request only necessary passport nationality/type and relevant visa/residence status, never numbers. Verify uncertain entry/transit requirements against current official sources for the **specific connection**, or label unresolved. An OTA badge is a platform statement, not a universal legal conclusion.

## Evidence, revisions and output

Read [reporting and the ledger](references/results.md). Log queries with revision, family, airports/dates, source, timestamp, currency/party/account basis and evidence level. Loading failures and login walls are not “no flights.” Do not reject a date query because its cheapest flight misses a deadline while other timings remain unexamined.

When a rule changes, create a new revision, retain earlier files/quotes and reassess affected cases. Historical quotes remain historical, never “freshly verified.” A price change between checks is not automatically a date/weekday effect.

Present the lowest verified **eligible** fare, a practical low-fare alternative, and tradeoffs such as fewer hotel nights or included bags. Keep accepted soft-constraint exceptions separate, including the observed cheapest when useful. Never recommend a hard-deadline violation as eligible or call unresolved baggage/visa conditions confirmed.

Close with searched bounds, unresolved/blocked cases, outstanding timing checks, cost unknowns, timestamps and reproducible links. Say “lowest verified within the searched scope,” not “guaranteed cheapest.” Default to a compact shortlist plus full finalist legs. Save private research **outside this distributable repository**; never post user trips as public issues.

Booking, payment, account changes, publishing and ongoing monitoring require separate user instruction and host permissions.
