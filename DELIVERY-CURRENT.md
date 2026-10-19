# Current JEP delivery status

Updated 2026-10-19 (UTC). Core protocol **0.7 / Internet-Draft -07** and software package
versions are separate. Start with the
[released verifier and packaged sample](https://github.com/hjs-spec/jep-core#verify-your-first-event).

## Released components

| Component | Package / release | Scope |
| --- | --- | --- |
| Core verifier and BYOI | `jep-core-conformance==0.7.8` | GitHub and PyPI; local verification and scoped implementation tests |
| Local recorder | `jep-agent-sdk==2.1.8` | Optional local creation/export; no hosted API required |
| HTTP CLI | `jep-cli==0.7.2` | Requires a separately configured API |
| Python HTTP SDK | `jep-sdk-py==0.7.1` | Requires a separately configured API |
| JavaScript HTTP SDK | `@hjs-api-db/jep-sdk-js@0.7.2` | GitHub and npm; GitHub owner remains hjs-spec |
| Go HTTP SDK | `hjs-spec/sdk-go` v0.7.2 | HTTP transport, not an independent verifier |
| HTTP Quickstart | v0.7.2 | GitHub wheel/source; recording recovery requires API 0.8.6+ |
| Reference API | v0.8.7 | Source/container release; self-hosting available |

To create your own signed record with the optional recorder, follow the
[Agent SDK local example](https://github.com/hjs-spec/jep-agent-sdk#local-create--export--independent-verification).
For HTTP integrations, use the [component directory](PROJECTS.md#integrate).

## Adoption fixes verified on 2026-10-01

- [Agent SDK 2.1.8](https://github.com/hjs-spec/jep-agent-sdk/releases/tag/v2.1.8) accepts the existing string and array V scopes. CI passes on Python 3.10–3.13. A fresh PyPI installation passes all 29 selected BYOI producer/verifier checks through a disclosed SDK wrapper; eight acceptance checks are outside that run. GitHub and PyPI wheel/source hashes agree.
- [API 0.8.7](https://github.com/hjs-spec/jep-api/releases/tag/v0.8.7) preserves the original creation response for an unchanged caller-ID request. [Release checks](https://github.com/hjs-spec/jep-api/actions/runs/36807795504) include 132 tests with real PostgreSQL, migration, concurrent replicas and the container smoke check. Follow the [upgrade and recovery instructions](https://github.com/hjs-spec/jep-api/blob/main/DEPLOYMENT.md#upgrade-from-sqlite).
- [Quickstart 0.7.2](https://github.com/hjs-spec/jep-quickstart/releases/tag/v0.7.2) separates business completion from recording failure. Its [release tests](https://github.com/hjs-spec/jep-quickstart/actions/runs/36808099905) exercise recovery over real HTTP against the pinned API 0.8.7 commit; recovery resends the saved recording request without rerunning the callable.
- API 0.8.7 supplies MIT terms for original code and retains BSD-3-Clause for Core schema/fixture copies. [Python SDK 0.7.1](https://github.com/hjs-spec/sdk-py/releases/tag/v0.7.1) supplies its declared MIT license; Quickstart 0.7.2 supplies BSD-3-Clause. Full license texts and scope notices are checked in source, wheel and container distributions as applicable. Downloaded Python SDK artifacts match the GitHub release digests and pass all 10 client tests; downloaded Quickstart artifacts pass all 18 real-HTTP tests against the downloaded API source.
- [Contribution routes](CONTRIBUTING.md) and [private security reporting](SECURITY.md) are shared across component repositories. Component-specific guides retain their development instructions. The [first-use check and feedback form](https://github.com/hjs-spec/jep-core/blob/main/docs/FIRST-USE-CHECK.md) cover verification, local creation, HTTP and BYOI through existing guides.

- **Main-branch enforcement is active in all eight primary repositories.** The [ruleset IDs and checks](maintenance/branch-rules/README.md) were verified on 2026-10-01: all eight report `protected: true`, 24 required GitHub Actions checks match the reviewed inputs, and no bypass actors are configured. Merging requires a PR, an up-to-date branch and resolved review conversations; force pushes and deletion are blocked. Required approvals remain zero for the single-maintainer workflow. [Core #44](https://github.com/hjs-spec/jep-core/pull/44) verified the normal PR path: 12 checks appeared as Required, merging was disabled while checks were running, and the PR merged after all 12 passed.

These are implementation and adoption corrections. Core 0.7 semantics and frozen
specification artifacts are unchanged.

## Remaining adoption work

- **Real-workflow first-use evidence still requires participants.** An independently authored implementation and reproducible fixture report now exist (see below). Maintainer reruns and JEP-owned bridges are disclosed separately; they do not establish real deployment, organizational adoption or production effects.
- The existing ClawHub `schchit/judgment-event-protocol` listing has a prepared replacement; publication requires confirmation of ClawHub's MIT-0 license and upload through the owner account. The website developers copy needs the prepared terminology patch applied in its existing project.

## Core software 0.7.8

- [Release #52](https://github.com/hjs-spec/jep-core/pull/52) publishes the optional BYOI `--state-setup` hook and current installation instructions. [GitHub 0.7.8](https://github.com/hjs-spec/jep-core/releases/tag/v0.7.8) provides the source, wheel and explicit legacy Go binaries. The [publication and installed-release run](https://github.com/hjs-spec/jep-core/actions/runs/39194682391) records successful PyPI publication and the registry installation outcomes. GitHub/PyPI wheel and source SHA-256 digests agree.
- [External publication sources #53](https://github.com/hjs-spec/jep-core/pull/53) retain the replacement ClawHub skill and exact website developers copy corrections. Their merge does not publish either external page.

## Independent implementation and October follow-up

- [Probity report #47](https://github.com/hjs-spec/jep-core/issues/47) supplies independently authored Core 0.7 producer, verifier and synthetic acceptance processing. The [fixed pilot #48](https://github.com/hjs-spec/jep-core/pull/48) pins reader commit `cbd3ea8f4de89b835d6d3c4182ff4b4b1c7608f9` and the agreed suite; its 37 selected checks and deliberate-fault controls pass.
- [Native BYOI integration #50](https://github.com/hjs-spec/jep-core/pull/50) adds an optional disposable-state setup hook and an explicitly JEP-owned bridge. The unchanged pinned reader passes 25 verifier, four producer and eight acceptance checks. Bridge mappings and synthetic ledger effects are disclosed in the [reproduction guide](https://github.com/hjs-spec/jep-core/blob/main/docs/PROBITY-NATIVE-BYOI.md).
- Contributor [candidate check #49](https://github.com/hjs-spec/jep-core/pull/49), integrated through [#51](https://github.com/hjs-spec/jep-core/pull/51), tests candidate code against frozen agreed cases, candidate cases and the pinned separate reader. Source-fault, poisoned-expectation and suite-metadata controls pass. All four integration PR workflow runs passed. This does not add a required branch check or change Core requirements.
- Frozen Core/Profiles/Conformance publications, signed vectors and BYOI suite bytes remain unchanged. Test evidence covers selected public fixtures and isolated synthetic state; it does not establish external authorization or business effects.

## Verification evidence for Core software 0.7.7

- [Core #38](https://github.com/hjs-spec/jep-core/pull/38) implements the usable installed path, current schema alignment and documentation cleanup. Its CI verifies the README commands outside the checkout on Linux, Windows and macOS, plus current/legacy conformance and ecosystem interoperability.
- [GitHub Release](https://github.com/hjs-spec/jep-core/releases/tag/v0.7.7) and [PyPI](https://pypi.org/project/jep-core-conformance/0.7.7/) publish the source and wheel. Original GitHub/PyPI artifact hashes agree.
- [Post-publication installation checks](https://github.com/hjs-spec/jep-core/actions/runs/36740810755) passed on Linux, Windows and macOS using the actual published release set. CI reports and downloaded-byte checksums are attached to that run.
- The packaged sample and 29-check demo were also run from a fresh public PyPI installation. The BYOI suite remains version 1.0.0, digest `sha256:b05b6284f591f74e35065d24ef44466e610304134ca42416dbf2a6b8e4232565`.

See each report for its exact versions, artifacts and validation scope.

## History

The [previous maintained snapshot](https://github.com/hjs-spec/.github/blob/dacd2dcac038a21a8ee20e73cee145fda6ed5a1b/DELIVERY-CURRENT.md)
preserves the earlier release set, checks and operational decisions. Other dated
records remain unchanged: [2026-09-26 audit](DELIVERY-2026-09-26-HISTORICAL.md),
[2026-09-27 closeout](DELIVERY-2026-09-27.md) and [hardening evidence](DELIVERY-2026-09-27-HARDENING.md).
Published IETF artifacts and historical signed records are immutable.
