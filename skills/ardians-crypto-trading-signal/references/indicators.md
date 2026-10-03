# Indicators and Data Ingestion

Detail for `ardians-crypto-trading-signal`.

## Data ingestion

- Source: record the exchange or data provider, the endpoint, and the retrieval
  time.
- Instrument: record symbol, quote currency, and contract or spot.
- Timeframe: record the bar size and the timezone. Normalize everything to UTC.
- Coverage: record the start and end of the series and the number of bars.
- Gaps and duplicates: detect missing bars and duplicate timestamps, then state
  how each was handled (drop, forward-fill, or reject).
- Adjustments: state whether volume or price is adjusted and how.

## Indicator computation

Implement indicators from the series so they are testable and inspectable.

- Moving averages: simple and exponential, with an explicit warm-up period.
- Momentum: RSI and rate of change, with the lookback stated.
- Volatility: ATR, rolling standard deviation, and realized volatility.
- Volume: volume moving average and relative volume.
- Bands and channels: Bollinger Bands and Donchian channels.

Rules:

- The first `n` bars of a rolling window are undefined. Never treat them as zero.
- The indicator at bar `t` may use only data available at or before `t`.
- Test each indicator against a hand-computed fixture, including the warm-up
  boundary.

## Environment

Use `uv` to pin the Python version and dependencies so results are reproducible.
Keep data ingestion, indicator computation, and strategy logic in separate
modules so each can be tested alone.
