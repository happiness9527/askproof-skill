# Sample Handoff

Fictional project: TinyInvoice.

## Current Task Goal

Make TinyInvoice export invoices as PDF.

## Completed Work

- Added an “Export PDF” button.
- Connected the button to a PDF export function.
- AI claims it fixed a missing PDF renderer dependency.

## Verified Work

- No verification evidence provided yet.

## Unverified Work

- Whether clicking the button downloads a PDF.
- Whether invoice totals are correct.
- Whether customer name, invoice number, and tax fields render correctly.
- Whether the invoice list page still works.

## Current Risks

- The AI may have changed code without verifying the user-facing flow.
- Continuing with new features may hide the original problem.

## Key Decisions

- Verify PDF export before adding batch export or template styling.
- Ask for minimum proof instead of accepting “should work now”.

## Next Copy-Ready Prompt

```text
Please continue from this handoff. The current goal is to make TinyInvoice export invoices as PDF. First restate the completed, verified, unverified, and risky parts. Do not add new features yet. Give the smallest verification step that proves the Export PDF button downloads a correct PDF.
```

## Do Not Repeat

- Do not accept “should work now” without evidence.
- Do not add batch export before single export is verified.
- Do not refactor unrelated pages before the current issue is understood.

