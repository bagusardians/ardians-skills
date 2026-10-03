# Backtesting

Detail for `ardians-crypto-trading-signal`. A backtest is only meaningful if it
controls for bias and cost.

## Look-ahead bias

- A decision at bar `t` may use only data closed at or before `t`.
- Do not use the current bar's close to decide an entry at the current bar's
  open.
- Shift indicator inputs when there is any doubt, and test the shift.
- Beware survivorship bias: include delisted or failed instruments when the
  strategy universe would have included them.

## Costs

- Fees: apply the taker and maker fee that the venue actually charges.
- Slippage: model it as a function of order size and liquidity, not a fixed
  guess.
- Funding: for perpetuals, include funding payments.
- Spread: use the bid and ask when available.

Report results with and without costs. A strategy that is only profitable before
costs is not viable.

## Evaluation

- Split the data into in-sample and out-of-sample segments. Tune only on
  in-sample.
- Use walk-forward analysis to test stability across time.
- Report the equity curve, max drawdown, Sharpe and Sortino ratios, hit rate,
  and average win and loss.
- Test parameter sensitivity: a strategy that only works at one parameter value
  is overfit.
- Compare against a buy-and-hold baseline.

## Reproducibility

Use `jupyter` for the analysis and keep the notebook deterministic. Pin the data
snapshot, the code version, and the parameters. State the exact window for every
number reported.
