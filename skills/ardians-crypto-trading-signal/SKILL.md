---
name: ardians-crypto-trading-signal
description: Builds and evaluates crypto trading signals and strategies, including data ingestion, indicators, backtesting, risk management, and signal delivery. Use when the user mentions a crypto trading signal, a trading bot, a trading strategy, backtest a strategy, or a market signal. Not financial advice.
triggers:
- crypto trading signal
- trading bot
- trading strategy
- backtest a strategy
- market signal
---

# Ardians Crypto Trading Signal

A specialized, on-demand skill. It is not part of the default product pipeline
and is invoked only for crypto, trading, or market-signal requests.

This is engineering guidance, not financial advice. Never present a signal as a
recommendation to trade.

## Safety boundaries

These are hard rules.

- Do not place a live trade, or call a live order endpoint, without explicit
  confirmation for that specific order.
- Paper-trade or backtest first. Live execution requires a separate, explicit
  decision by the user.
- Store exchange API keys and secrets as secrets. Never hardcode, log, commit,
  or print them. Prefer read-only keys; never enable withdrawals.
- State the failure modes: overfitting, look-ahead bias, survivorship bias,
  regime change, liquidity, and fees. Quantify them where possible.
- Label every result with its data window, costs, and assumptions.

## Workflow

1. **Define the hypothesis.** State the market, instrument, timeframe, and the
   edge being tested. Invoke `brainstorming` if the objective is vague.
2. **Get the data.** Ingest OHLCV and any auxiliary series. Record source,
   symbol, timeframe, timezone, and coverage. Handle gaps, duplicates, and
   timezone alignment explicitly. See `references/indicators.md`.
3. **Compute indicators.** Implement indicators from the data, not from a black
   box, and test them. Invoke `test-driven-development` for indicator and
   pipeline code. Use `uv` for a reproducible Python environment.
4. **Backtest with controls.** Prevent look-ahead bias, apply fees and slippage,
   and use out-of-sample and walk-forward evaluation. Invoke `jupyter` for the
   analysis. See `references/backtesting.md`.
5. **Manage risk.** Define position sizing, stop and take-profit rules, max
   drawdown, and exposure limits before evaluating returns. See
   `references/risk.md`.
6. **Score the signal.** Use `use-jev` for typed classification or scoring where
   a signal needs a decision or a confidence. Invoke `evidence-based-citations`
   for any external claim about an indicator or a market.
7. **Deliver and monitor.** Define how signals reach the user, with timestamp,
   instrument, direction, confidence, and invalidation. Invoke `datadog` for
   monitoring and `openhands-automation` for scheduled runs. See
   `references/signal-delivery.md`.
8. **Protect the system.** Invoke `security` for secret storage, least
   privilege, and endpoint hardening.

## References

- `references/indicators.md`: data ingestion and indicator computation.
- `references/backtesting.md`: bias, costs, and evaluation.
- `references/risk.md`: sizing and exposure rules.
- `references/signal-delivery.md`: output format and monitoring.

## Reporting

Always report: data window, instruments, timeframe, costs assumed, in-sample
versus out-of-sample results, max drawdown, and the conditions under which the
signal fails. Never report a headline return without the drawdown and the
out-of-sample number beside it.
