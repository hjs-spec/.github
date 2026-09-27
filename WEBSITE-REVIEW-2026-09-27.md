# Public website review — 2026-09-27

Scope: https://www.humanjudgment.org and apex-domain redirects, read-only. No deployment, cache purge, DNS write or search-console submission is authorized by a passing audit job alone.

Cached search extracts mixed a current 0.7 homepage with older developers/architecture and historical governance/alignment/primitives copy. This is a lead to verify, not proof of the current source tree. A failed fetch is likewise not proof of a deleted page.

A small, non-scheduled audit workflow captures fresh public HTTP status, redirect targets, selected non-sensitive cache/server headers, body digests, HTML titles/descriptions/canonical links and visible-text indicators. Raw bodies are saved as workflow evidence. It does not execute site JavaScript; a client-rendered shell cannot establish route text. Optional old routes returning 404/410 are acceptable. Errors are recorded rather than silently converted to successful checks.

## Required content checks

| Route | Acceptance check |
|---|---|
| `/`, `/protocol` | Current protocol entry and explicit boundaries; no unsupported production-service claim |
| `/developers` | Stable event `id`; no Core-required nonce; actual detached-JWS example or link to runnable SDK example; independent result checks |
| `/architecture` | Event Identity separate from Event Hash; no legacy mandatory-field list presented as current |
| `/governance`, `/alignment`, `/primitives` | Either current accurate material, explicit historical labeling, or redirect/retirement; no unqualified zero-PII, automatic legal-compliance/circuit-break, sovereign witness, or unmeasured performance guarantees |
| `/robots.txt`, `/sitemap.xml` | Current intended discoverable routes only; metadata and canonical routing must agree |

A term match is not itself a defect: a page may correctly say that Core does **not** require a nonce or that signatures do **not** prove authorization. Review the full surrounding text before changing content.

## Source and deployment access

The current GitHub connection's accessible repository inventory and scoped code searches did not identify a website repository or deployment project for this domain. That does not prove no source exists. Do not edit Prooftask, an unrelated app, or a guessed repository as a substitute. Identify the owning site project before changing routes, metadata, redirects or cache settings.

Final fresh-audit observations are to be appended after the workflow finishes. Until then this file is an acceptance checklist, not a completed website fix. [Current delivery](DELIVERY-CURRENT.md).
