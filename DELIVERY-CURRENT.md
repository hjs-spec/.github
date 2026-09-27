# Current JEP delivery status

Updated 2026-09-27. This is the maintained status entry, not a replacement for dated test reports. Core protocol 0.7 / Internet-Draft -07 and software package versions are separate. No hosted API is required for local creation, export and independent verification.

## Current installation choices

| Component | Package / release | Delivery and scope |
|---|---|---|
| Core verifier | `jep-core-conformance==0.7.5` | GitHub and PyPI; current Python verifier, explicit 0.6 compatibility |
| Local recorder | `jep-agent-sdk==2.1.6` | GitHub and PyPI; no hosted API required |
| CLI | `jep-cli==0.7.2` | GitHub and PyPI; HTTP client, not a local signer |
| Python HTTP SDK | `jep-sdk-py==0.7.0` | GitHub and PyPI; requires a separately configured API |
| JavaScript HTTP SDK | `@hjs-api-db/jep-sdk-js@0.7.2` | GitHub and npm; new npm scope, GitHub owner remains hjs-spec |
| Go HTTP SDK | `hjs-spec/sdk-go` v0.7.2 | GitHub/module tag; HTTP transport, not an independent verifier |
| HTTP Quickstart | v0.7.0 | GitHub package; local API setup is separate |
| Reference API | v0.8.5 | Source/container release; self-hosting available, maintainer production hosting deferred |

Minimal local installation:

```sh
python -m pip install jep-core-conformance==0.7.5 jep-agent-sdk==2.1.6
```

Use a new environment. Do not install historical `jep-v06-conformance-seed` beside the current Core package: both own `jep_conformance`. Current Core includes `jep-validate-06` for explicitly selected legacy input. Third-party dependencies require network access unless separately supplied.

For a first usable signed record, follow the [local SDK example](https://github.com/hjs-spec/jep-agent-sdk#local-create--export--independent-verification). For HTTP integration, use [Quickstart](https://github.com/hjs-spec/jep-quickstart) and configure your own endpoint. Installing an HTTP client does not start or configure a service.

## What has been verified

The [hardening closeout](DELIVERY-2026-09-27-HARDENING.md) records publication and three-platform installation of Core 0.7.5 / SDK 2.1.6 with API 0.8.5. Its JavaScript member was the historical 0.7.1 tarball; that old report is not evidence for a changed combination.

The [npm closeout](https://github.com/hjs-spec/sdk-js/blob/main/PUBLISHING.md) records independent public downloads and a clean, credential-free install of the actual new-scope 0.7.2 tarball. Its bytes matched the GitHub artifact. The owner subsequently confirmed that the Trusted Publisher was added and the temporary tokens/secret removed; that is owner confirmation, not a read-back or an actual OIDC upload test.

The current combined gate is updated in [Core #34](https://github.com/hjs-spec/jep-core/pull/34): actual release commits, new npm scope, Linux/Windows/macOS installs, signature/hash transport and unchanged Binding/02 reproduction pins. Final check links are recorded in the PR; only completed passing runs count as evidence. Historical reports and files are not relabeled as this new set.

## Deployment and credentials

Maintainer-operated API hosting is deferred by the owner. The isolated Railway API, PostgreSQL service and persistent volume were removed and absence from the active resource inventory was checked. Backend retention and final billing are outside that inventory check. The original Hugging Face Space was left unchanged and is not a current production endpoint. No credentials or infrastructure need to be supplied for the local path.

[API #16](https://github.com/hjs-spec/jep-api/pull/16) removes automatic Hugging Face deployment after software releases; future hosting is manual opt-in with existing security/readiness checks. [JavaScript #15](https://github.com/hjs-spec/sdk-js/pull/15) retires the one-time npm bootstrap outside active workflows, preserving exact historical source. Normal releases and read-only package verification remain available.

Do not provision resources, recreate bootstrap tokens, repeat npm/PyPI uploads or test OIDC by republishing an existing version. Actual token-free npm publication is a next-intended-release acceptance item, not a present success claim.

## Publication-page and website limits

Core #34 fixes README links and adds package project URLs in source for the next intended release. Already-uploaded PyPI metadata has not been replaced and the same version must not be overwritten. Current usable documentation is linked above.

The separate [website audit](WEBSITE-REVIEW-2026-09-27.md) distinguishes fresh public HTTP observations from cached search results. A site audit does not modify website source, purge its cache or resubmit search indexes.

## Preserved evidence

- [2026-09-26 original audit](DELIVERY-2026-09-26-HISTORICAL.md)
- [2026-09-27 earlier installation closeout](DELIVERY-2026-09-27.md)
- [2026-09-27 implementation hardening](DELIVERY-2026-09-27-HARDENING.md)
- [Earlier owner configuration instructions, historical only](CONFIGURATION-HANDOFF-2026-09-27-HISTORICAL.md)

Published IETF/TSTO artifacts, historical signed records, archived experiments, unrelated services and Prooftask are outside this closeout. [Repository directory](PROJECTS.md) · [Owner handoff](CONFIGURATION-HANDOFF-2026-09-27.md).
