# Contributing to JEP

Choose the route that matches your contribution:

| Contribution | Where and what to submit |
|---|---|
| Software bug, setup problem or documentation correction | Open an issue in the affected repository with the package version or commit, command, expected result and actual result. Use a minimal example with synthetic data. Small documentation fixes can go directly to a pull request. |
| Specification ambiguity | [Core issue](https://github.com/hjs-spec/jep-core/issues/new): identify the draft, section and conflicting behavior. |
| Independent implementation | [Implementation report](https://github.com/hjs-spec/jep-core/issues/new?template=independent-implementation.yml): identify the implementation, version, supported roles and reused libraries. |
| Interoperability results | Run the [BYOI guide](https://github.com/hjs-spec/jep-core/blob/main/docs/BYOI-CONFORMANCE.md), then attach the report and reproducible commands to an [interop result](https://github.com/hjs-spec/jep-core/issues/new?template=interoperability-result.yml). |
| Security-sensitive issue | Follow [SECURITY.md](SECURITY.md); report privately. |

For code changes, follow the affected repository's development instructions and
include the relevant test results in your pull request. Preserve existing signed
artifacts. Core 0.7 remains in its feature-stability period; see the
[Core contribution policy](https://github.com/hjs-spec/jep-core/blob/main/CONTRIBUTING.md#changes).
