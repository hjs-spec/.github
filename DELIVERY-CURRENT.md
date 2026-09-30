# Current JEP delivery status

Updated 2026-09-30 (UTC). Core protocol **0.7 / Internet-Draft -07** and software package
versions are separate. Start locally with the released verifier and packaged examples.

## First successful verification

Use Python 3.10 or later in a fresh environment:

```sh
python -m pip install jep-core-conformance==0.7.7
jep-byoi export jep-example
jep-validate validate jep-example/vectors/J-basic.json --keys jep-example/keys.json
jep-byoi demo --report byoi-reference-report.json
```

The sample returns `valid`. The demo reports 25 verifier assertions and four
producer checks using the bundled reference adapter. It identifies the tested roles
and reference reuse; acceptance scenarios are not selected. It is not independent
adoption or acceptance-effect evidence.
Use a new export directory. No account, hosted API, checkout or companion SDK is required.

Continue through the [implementer guide](https://github.com/hjs-spec/jep-core/blob/main/docs/IMPLEMENTER-GUIDE.md),
[BYOI adapter path](https://github.com/hjs-spec/jep-core/blob/main/docs/BYOI-CONFORMANCE.md)
and [report submission routes](https://github.com/hjs-spec/jep-core/blob/main/CONTRIBUTING.md).
Do not install historical `jep-v06-conformance-seed` beside the current package;
use the included `jep-validate-06` only for explicitly selected historical input.

## Released components

| Component | Package / release | Scope |
| --- | --- | --- |
| Core verifier and BYOI | `jep-core-conformance==0.7.7` | GitHub and PyPI; local verification and scoped implementation tests |
| Local recorder | `jep-agent-sdk==2.1.6` | Optional local creation/export; no hosted API required |
| HTTP CLI | `jep-cli==0.7.2` | Requires a separately configured API |
| Python HTTP SDK | `jep-sdk-py==0.7.0` | Requires a separately configured API |
| JavaScript HTTP SDK | `@hjs-api-db/jep-sdk-js@0.7.2` | GitHub and npm; GitHub owner remains hjs-spec |
| Go HTTP SDK | `hjs-spec/sdk-go` v0.7.2 | HTTP transport, not an independent verifier |
| HTTP Quickstart | v0.7.0 | Optional local API setup |
| Reference API | v0.8.5 | Source/container release; self-hosting available |

To create your own signed record with the optional recorder, follow the
[Agent SDK local example](https://github.com/hjs-spec/jep-agent-sdk#local-create--export--independent-verification).
For HTTP integrations, use the [component directory](PROJECTS.md#integrate).

## Verification evidence for Core software 0.7.7

- [Core #38](https://github.com/hjs-spec/jep-core/pull/38) implements the usable installed path, current schema alignment and documentation cleanup. Its CI verifies the README commands outside the checkout on Linux, Windows and macOS, plus current/legacy conformance and ecosystem interoperability.
- [GitHub Release](https://github.com/hjs-spec/jep-core/releases/tag/v0.7.7) and [PyPI](https://pypi.org/project/jep-core-conformance/0.7.7/) publish the source and wheel. Original GitHub/PyPI artifact hashes agree.
- [Post-publication installation checks](https://github.com/hjs-spec/jep-core/actions/runs/36740810755) passed on Linux, Windows and macOS using the actual published release set. CI reports and downloaded-byte checksums are attached to that run.
- The packaged sample and 29-check demo were also run from a fresh public PyPI installation. The BYOI suite remains version 1.0.0, digest `sha256:b05b6284f591f74e35065d24ef44466e610304134ca42416dbf2a6b8e4232565`.

These results cover the named roles and assertions. They do not establish actor
trust, external truth, legal validity, complete profile coverage or a hosted deployment.
The current PyPI README contains the released installation path; earlier package
versions and their metadata remain unchanged.

## Separate operational work

Maintainer-operated API hosting remains deferred. Local verification needs no
new database, signing identity or hosting resources. A future hosted deployment
requires its own explicit decision and deployment checks.

The [owner handoff](CONFIGURATION-HANDOFF-2026-09-27.md) records the separate npm
publisher and website work. No new npm release or website deployment is claimed
by this Core release. The [2026-09-27 website audit](WEBSITE-REVIEW-2026-09-27.md)
is dated evidence, not a fresh website review.

## History

The [previous maintained snapshot](https://github.com/hjs-spec/.github/blob/79fadc545740a746d00482e1176fb9fbc8ae12a9/DELIVERY-CURRENT.md)
preserves the earlier release set, checks and operational decisions. Other dated
records remain unchanged: [2026-09-26 audit](DELIVERY-2026-09-26-HISTORICAL.md),
[2026-09-27 closeout](DELIVERY-2026-09-27.md) and [hardening evidence](DELIVERY-2026-09-27-HARDENING.md).
Published IETF artifacts and historical signed records are immutable.
