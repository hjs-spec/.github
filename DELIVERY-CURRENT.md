# Current JEP delivery status

Updated 2026-09-30 (UTC). Core protocol **0.7 / Internet-Draft -07** and software package
versions are separate. Start with the
[released verifier and packaged sample](https://github.com/hjs-spec/jep-core#verify-your-first-event).

## Released components

| Component | Package / release | Scope |
| --- | --- | --- |
| Core verifier and BYOI | `jep-core-conformance==0.7.7` | GitHub and PyPI; local verification and scoped implementation tests |
| Local recorder | `jep-agent-sdk==2.1.7` | Optional local creation/export; no hosted API required |
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

See each report for its exact versions, artifacts and validation scope.

## History

The [previous maintained snapshot](https://github.com/hjs-spec/.github/blob/79fadc545740a746d00482e1176fb9fbc8ae12a9/DELIVERY-CURRENT.md)
preserves the earlier release set, checks and operational decisions. Other dated
records remain unchanged: [2026-09-26 audit](DELIVERY-2026-09-26-HISTORICAL.md),
[2026-09-27 closeout](DELIVERY-2026-09-27.md) and [hardening evidence](DELIVERY-2026-09-27-HARDENING.md).
Published IETF artifacts and historical signed records are immutable.
