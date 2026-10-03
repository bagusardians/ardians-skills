# Signal Delivery and Monitoring

Detail for `ardians-crypto-trading-signal`.

## Signal format

Every signal states:

- Timestamp (UTC) and the bar it is based on.
- Instrument and timeframe.
- Direction or state (long, short, flat, or a score).
- Confidence or score, with the method that produced it.
- Entry reference, invalidation level, and any target.
- The assumption that would void the signal.

Use `use-jev` when a signal needs a typed decision or a probability.

## Delivery

- Choose the channel the user names, such as a report, a message, or a file.
- Keep the signal log append-only so history can be audited.
- Never place an order as part of delivery. Delivery is information, not
  execution.

## Monitoring

- Invoke `datadog` to monitor data freshness, signal latency, and error rates.
- Alert on stale data, a signal that cannot be computed, and any execution
  anomaly.
- Track realized versus expected behavior so drift is visible.

## Scheduled runs

- Invoke `openhands-automation` for recurring runs (for example, on each bar
  close).
- Make runs idempotent: a repeated run must not emit a duplicate signal.
- Store credentials as secrets and grant the automation the least privilege it
  needs.

## Reporting discipline

Never report a headline return without the drawdown and the out-of-sample
number beside it. Label every signal as engineering output, not financial
advice.
