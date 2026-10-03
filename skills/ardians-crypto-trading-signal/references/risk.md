# Risk Management

Detail for `ardians-crypto-trading-signal`. Define risk before evaluating
returns.

## Position sizing

- Risk a fixed fraction of equity per trade, for example 1 percent. State the
  number explicitly.
- Derive size from the distance between entry and stop, not from a target
  notional.
- Cap total exposure across correlated positions. Crypto assets are often highly
  correlated; treat them as one risk bucket where they are.

## Stops and exits

- Every position has an invalidation level defined before entry.
- Define take-profit and trailing rules, or state that exits are signal-driven.
- Handle gaps through the stop: the fill may be worse than the stop price.

## Portfolio limits

- Max drawdown: set a level at which trading halts and requires review.
- Max concurrent positions and max exposure per asset.
- Leverage: state it, cap it, and model liquidation.

## Failure modes

- Overfitting: the strategy fits noise in the sample.
- Regime change: the edge disappears when market conditions change.
- Liquidity: the assumed size cannot be filled at the assumed price.
- Execution: latency, partial fills, and outages.

## Hard rules

- No live order without explicit confirmation for that order.
- Paper-trade or backtest before any live run.
- Exchange keys are read-only with withdrawals disabled, stored as secrets.
