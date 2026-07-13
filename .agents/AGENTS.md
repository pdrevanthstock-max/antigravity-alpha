# AutoTrader Customization Rules

These rules enforce strict backtest verification, pre-flight checks, and fallback observability.

## Pre-flight & Fallback Rules
1. **Pre-flight Token Check**: Verify the Dhan access token by running a cheap query before initiating a backtest or live run. Fail fast with an authentication error if the token is invalid.
2. **Observability of Offline Cache**: If a run falls back to cache because of API failure, log it as an `ERROR` and display a clear header banner in the Streamlit interface warning that cached data is being used.
3. **Evidence-based Verification**: Never state that a task is verified or resolved without outputting the exact command-line executions and terminal logs.
