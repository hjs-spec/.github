# Public website review — 2026-09-27

Scope: https://www.humanjudgment.org and apex-domain redirects, read-only. No website deployment, cache purge, DNS write or search-console submission was performed. The original Hugging Face Space and Prooftask were not changed.

## Evidence

The [fresh HTTP audit](https://github.com/hjs-spec/.github/actions/runs/36299281135) requested 11 fixed public URLs at **06:09:49–06:09:51 UTC**. The downloaded [audit artifact](https://github.com/hjs-spec/.github/actions/runs/36299281135/artifacts/10924604596) has SHA-256 `4aa1c5694868759f56cfeeb6a355e0fea9398f530ed1b0ceec06338c241a8a96`. It contains the response report, original HTTP bodies and extracted visible text. Full surrounding text was reviewed, not just keyword matches.

This proves what those public endpoints served in that observation, not the state of a source repository or all geographical caches. Requesting no-cache did not guarantee bypass of Vercel caches: some replies were HIT; alignment and primitives returned PRERENDER with age 0. The response server was Vercel. This does not identify the owning Vercel account or project.

## Confirmed findings

| Route | Observed state | Required action |
|---|---|---|
| `/` and `/protocol` | HTTP 200; current 0.7 structure, Event Identity, independent checks and explicit boundaries are present | Preserve current content; do not redo the old six-field migration |
| `/developers` | HTTP 200; 11 standard members, seven unconditionally required, no Core-required nonce and independent checks are already described | Repair the remaining example and qualification issues below, not the whole page |
| `/architecture` | HTTP 200; current 11-member list and Event Identity are present | Preserve the updated structure |
| `/governance` | HTTP 200; sandbox page still includes unqualified sovereign-witness, zero-PII, automatic circuit-break and performance claims | Remove obsolete claims or retire the route; a sandbox label does not qualify universal claims elsewhere on the page |
| `/alignment` | HTTP 200; legal-to-logic and compliance simulation plus the same universal claims | Retire or clearly distinguish a non-operative historical simulation from current protocol guarantees |
| `/primitives` | HTTP 200; sidecar interception and runtime/compliance behavior presented as primitive functionality | Replace with current primitive semantics or redirect to `/protocol`; retain history outside the current protocol entry |
| `/robots.txt` and `/sitemap.xml` | HTTP 404 | Add intended crawler/sitemap documents in the owning site project; their absence is not proof that search engines cannot index the site |
| Apex `/` and `/developers` | Redirected to www; final bodies match direct www requests | Preserve working canonical-domain routing |

All seven content routes used the same generic description in these HTTP responses; no HTML canonical link was observed. Route-specific descriptions and canonical metadata are a follow-up for the owning site. This is not a ranking guarantee.

### Remaining developer-example issues

The visible example uses a `ref` array, whereas the [current structural schema](https://github.com/hjs-spec/jep-core/blob/main/schemas/jep-event.schema.json) accepts a typed reference object or digest. It also uses an object-shaped placeholder signature with an `EdDSA` header and no demonstrated key binding, rather than the current implemented detached-JWS baseline. Core allows profile-defined signature containers, so the object shape alone is not a universal Core violation; the example nevertheless must not be presented as a runnable example of the current baseline.

Prefer linking to or importing a real output from the [versioned local SDK create/export/verify example](https://github.com/hjs-spec/jep-agent-sdk#local-create--export--independent-verification). Use valid `ref` form, actual baseline signature syntax and explicit verification material, or visibly label abbreviated strings as non-verifiable illustrations. Do not supply a private key or claim that a co-shipped public key independently proves actor identity. Distinguish the supported baseline algorithms and sample error vocabulary from all possible protocol profiles.

### Obsolete route claims

The three old routes continue to say that every action is witnessed by a sovereign node, that no personal data ever touches the protocol, that termination provides an atomic runtime kill-switch, and that latency/throughput meet specific universal targets. Those claims are not established by the current protocol and no corresponding deployment/benchmark evidence was supplied in the site. Do not attribute legal compliance decisions, automatic enforcement or universal privacy properties to Core. No jurisdictional legal analysis is asserted by this audit.

For minimum maintenance, redirect retired routes to the accurate protocol or architecture page and remove their old navigation/sitemap entries. If preservation in-place is necessary, label the entire page as a historical non-operative simulation and remove unsupported current-service promises. Merely hiding the route from navigation is insufficient while its public URL still returns the claims.

## Source and deployment access

The current GitHub connection's accessible repository inventory and scoped code searches did not identify the website source repository. That does not prove no source exists. Do not edit Prooftask, an unrelated app or a guessed repository as a substitute.

The public responses identify Vercel as the host. After the owner installed Vercel at 06:16 UTC, plugin discovery confirmed `installed: true`. However, action discovery still returned no Vercel namespace, project-reading action or deployment action in this session. This is a tool-exposure limitation, not evidence that the owner failed to install or authorize it. Do not ask the owner to repeat installation or share a token. When project actions become available, resolve the existing humanjudgment.org deployment and its source before making changes. An exact accessible source repository would also resolve source access. No new hosting account, paid plan, API database or package publication is needed.

## Completion boundary

The audit is complete for the named HTTP observations. Website changes are **not deployed**. A successful audit workflow means evidence was collected, not that every route conforms. After project/source access is available, change the identified site source, preserve the current 0.7 pages, deploy to that existing project, and rerun the same fixed-route check. Verify both domain forms and intended routes before requesting search re-indexing. Do not treat stale search extracts as the current source of truth.

[Current delivery](DELIVERY-CURRENT.md) · [Owner handoff](CONFIGURATION-HANDOFF-2026-09-27.md).
