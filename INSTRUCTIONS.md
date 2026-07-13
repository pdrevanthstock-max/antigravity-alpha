# AutoTrader Project Instructions and Verification Rules

You MUST read this file before writing any code, and cross-check it upon completion.

## Verification Mandate

### Rule 1: No claim without evidence
Never write "fixed," "verified," "working," or "all tests passing" without pasting the actual raw terminal/log output of the specific command that proves it. A narrative description of what should happen is not evidence. If you did not run it this session, say so explicitly.

### Rule 2: Reproduce, don't just report
Before declaring a bug fixed, run the exact scenario that originally failed (same date range, same capital, same config) and show the output changed. If you changed cache, config, or test data to get a passing result, explain exactly what changed and why.

### Rule 3: Diff against the spec
Before marking any feature "done," re-read the relevant section of `ARCHITECTURE.md` / `STRATEGIES.md` / `PAIR_SELECTION.md` / `EXECUTION.md` and confirm line-by-line that the implementation matches.

### Rule 4: Surface silent fallbacks loudly
Any time code falls back to cached/offline/synthetic data instead of the requested live source, this must be:
- Logged as an **ERROR**, not a warning, if it changes the meaning of the results (e.g. reduced strike scan range).
- Visible in the UI itself (via a warning banner).
- Called out explicitly in your response.

### Rule 5: State what you didn't check
End every change summary with an explicit "Not verified in this session" list.

### Rule 6: One change, one proof
When multiple bugs are fixed in one pass, show separate before/after evidence for each.

### Rule 7: Sanity-check numbers
Before presenting any backtest result (P&L, win rate, trade count), run one manual arithmetic check against the underlying data. If a number looks unusually good, flag it as needing investigation.

---

## Technical Constraints

1. **Pre-flight Token Validation**: Before any backtest, live, or paper run, verify Dhan credentials by making a fast, cheap live query (e.g. checking connection/expiry). If auth is invalid, fail fast with a clear error.
2. **Explicit Fallback Banners**: If cache-fallback mode is engaged, display a clear header banner in the Streamlit UI warning the user that they are running on reduced offline ATM-only cache.
3. **No Silent Scope Reduction**: Do not hide ATM-only cache restrictions. Raise errors or make the limitation extremely transparent.
