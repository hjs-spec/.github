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

## Current combination: completed verification

[Core #34](https://github.com/hjs-spec/jep-core/pull/34) is merged. Its checks use the actual API 0.8.5, Agent SDK 2.1.6 and new-scope JavaScript 0.7.2 release commits, with retained CLI/Go and Binding/02 reproduction pins.

- [Linux, Windows and macOS installations](https://github.com/hjs-spec/jep-core/actions/runs/36299156516): all three jobs passed. Each checked **13 original release files**, including four Python wheel/source pairs independently downloaded from PyPI and GitHub. The new-scope npm tarball was separately downloaded and compared to GitHub bytes and SHA-256/SHA-512/SHA-1 metadata. A credential-free npm install/import passed on each platform; Python wheels were installed with dependencies in a new environment.
- Installed Python smoke checks on all three platforms passed J/D/T/V signatures, four Core/SDK/CLI roundtrips, eight tamper rejections, eighteen malformed-input rejections, missing-key `indeterminate`, and accepted/already-accepted/identity-conflict behavior.
- [Current interoperability](https://github.com/hjs-spec/jep-core/actions/runs/36299156543): **11 signed events, five transport paths, 55 exact signed-artifact roundtrips, four verifiers and 50 Binding/02 structural/reference checks** passed. The paired Core/API/Agent boundary suite reports **25 passing cases**, including invalid-input rejection without consuming acceptance state. This is not 25 distinct vulnerabilities or a domain-policy/external-truth test.
- [Core current/legacy conformance](https://github.com/hjs-spec/jep-core/actions/runs/36299156499): passed, retaining frozen-publication checks and adding package-link/registry-selection/isolation guard tests.

Downloaded CI evidence ZIPs were checked against GitHub artifact digests; the included original release files were checked against the report digests. Reports, checksums and installation instructions remain downloadable from the runs. No release file was rebuilt or re-uploaded in this closeout.

The [earlier hardening closeout](DELIVERY-2026-09-27-HARDENING.md) included the historical JavaScript 0.7.1 tarball. It remains unchanged and is not relabeled as evidence for the new combined set. The script's explicit historical baseline is also preserved; the current CI uses `--current-release`.

## npm account and publishing boundary

The [npm closeout](https://github.com/hjs-spec/sdk-js/blob/main/PUBLISHING.md) records completed public first publication. The owner subsequently confirmed that the `release.yml` Trusted Publisher was added and the temporary tokens/secret removed; that is owner confirmation, not an independent account-setting read-back or an actual OIDC upload test.

[JavaScript #15](https://github.com/hjs-spec/sdk-js/pull/15) is merged after [passing tests](https://github.com/hjs-spec/sdk-js/actions/runs/36298984316). It removes the one-time bootstrap from active workflows and preserves its exact text outside that directory. Normal OIDC releases and read-only installation checks remain available. Do not provision resources, recreate bootstrap tokens, repeat existing npm/PyPI uploads or create a version solely to test OIDC. Actual token-free npm publication is a next-intended-release acceptance item.

## Hosted API remains deferred

[API #16](https://github.com/hjs-spec/jep-api/pull/16) is merged after [regression checks passed](https://github.com/hjs-spec/jep-api/actions/runs/36298878884). Hugging Face deployment no longer runs after software releases. A deliberate future deployment requires main, a manual run and exact confirmation `deploy-hosted-api`, and still must pass existing production configuration/readiness gates. Software tests, source releases and container builds are retained.

The isolated Railway API, PostgreSQL service and persistent volume were removed earlier and absence from active resource inventory was checked. Backend retention and final billing are outside that inventory check. The original Hugging Face Space was left unchanged and is not a current production endpoint. No credentials or infrastructure need to be supplied for the local path. This closeout provisions no new hosting resources and adds no scheduled monitoring.

## Publication-page and website limits

Core #34 fixes README links and adds package project URLs **in source for the next intended release**. Already-uploaded PyPI metadata has not been replaced and the same version must not be overwritten. Current usable documentation is linked above.

The [fresh website audit](WEBSITE-REVIEW-2026-09-27.md) confirms that the main protocol/architecture structure is already updated. Remaining work is narrower: the developer example, three old marketing/simulation routes, and absent robots/sitemap documents. The website responses identify Vercel; its owning project/source was not available through the current connection. The audit does not change website code, purge caches or resubmit search indexes. Website changes remain undeployed.

## Preserved evidence

- [2026-09-26 original audit](DELIVERY-2026-09-26-HISTORICAL.md)
- [2026-09-27 earlier installation closeout](DELIVERY-2026-09-27.md)
- [2026-09-27 implementation hardening](DELIVERY-2026-09-27-HARDENING.md)
- [Earlier owner configuration instructions, historical only](CONFIGURATION-HANDOFF-2026-09-27-HISTORICAL.md)

Published IETF/TSTO artifacts, historical signed records, archived experiments, unrelated services and Prooftask are outside this closeout. [Repository directory](PROJECTS.md) · [Owner handoff](CONFIGURATION-HANDOFF-2026-09-27.md).
