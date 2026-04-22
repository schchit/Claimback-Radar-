# Skill Definition: claimback_radar

## Description
Scans user emails and bills to discover hidden refunds, subscription traps, and savings opportunities.

## Functions

### Function 1: extract
Extracts structured subscription / billing data from unstructured text.

**Input**: Raw email or bill text
**Output**: `confirmation_card` (JSON)

### Function 2: detect_and_recommend
Detects risks and generates actionable receipts.

**Input**: `confirmation_card` + user context
**Output**: `action_receipts` + `risk_flags`

## Invocation Schema
See `schema/input.json`

## Output Schema
See `schema/output.json`

## Example
See `examples/netflix_email.md`
