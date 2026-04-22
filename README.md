# Claimback Radar

AI-powered inbox scanner for hidden refunds, subscription traps, and savings opportunities.

## What it does

**Function 1: Structured Extraction**
- Scans raw email / bill / subscription text and extracts: service name, provider, amount, billing cycle, next charge date, refund deadline, warranty expiry, cancellation method.

**Function 2: Risk Detection & Action Generation**
- Detects risks: upcoming charges, refund windows closing, unused services, price hikes, warranty expiring.
- Generates prioritized action receipts with deadlines and estimated savings.

## Quick Start

Paste an email or bill text into the Skill invocation:

```json
{
  "skill": "claimback_radar",
  "input": {
    "source": "email_text",
    "content": "Your raw email or bill text here...",
    "user_timezone": "Asia/Singapore",
    "current_date": "2026-04-22",
    "user_context": {
      "last_used_date": "2026-03-15",
      "monthly_budget": 50
    }
  }
}
```

## Output

- `confirmation_card`: Clean structured summary of the subscription / bill
- `action_receipts`: Prioritized todo list with deadlines, reasons, and savings estimates
- `risk_flags`: Alert tags (e.g., `refund_window_closing`, `unused_service`)

## Examples

- [Netflix subscription email](examples/netflix_email.md)
- [Amazon Prime renewal notice](examples/amazon_prime_email.md)

## Schema

- Input: [`schema/input.json`](schema/input.json)
- Output: [`schema/output.json`](schema/output.json)

## License

MIT
```
