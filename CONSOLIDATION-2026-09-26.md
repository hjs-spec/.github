# Maintenance consolidation — 2026-09-26

## Decision

Keep one protocol source in Core, one runnable introduction in Quickstart, and an
explicit choice between the API/HTTP clients and local Agent SDK recording.
Retire eight overlapping runtime, replay and observation experiments from active
development. Future signed recording and reports belong to the existing Agent SDK;
no new repository or package is introduced.

The organization still has 28 repositories: 11 archived and 17 unarchived, compared
with 3 archived and 25 unarchived before this step. Unarchived does not mean every
repository is a current Core implementation; research and historical integrations
retain their stated boundaries. No repository, source history or release was deleted.

## Retired repositories

Each repository received a retirement notice before its main branch was archived.
These baseline commits identify the code examined; the linked PR preserves the
decision in that repository's history.

| Repository | Code baseline | Retirement PR | Reason / retained capability |
|---|---|---|---|
| jep-replay-visualizer | `a945472df52e` | [#4](https://github.com/hjs-spec/jep-replay-visualizer/pull/4) | Separate browser projection; preserve its normalization and reader |
| jep-lineage-explorer | `dae2a0814bfa` | [#5](https://github.com/hjs-spec/jep-lineage-explorer/pull/5) | Separate declared lineage/scope model; preserve its checks |
| jep-runtime | `dcd5ef5b4ede` | [#10](https://github.com/hjs-spec/jep-runtime/pull/10) | Own envelope and mock signatures; preserve historical policy/replay |
| jep-authority-runtime | `70881c39d20b` | [#5](https://github.com/hjs-spec/jep-authority-runtime/pull/5) | Separate scope-policy experiment; preserve its policy evaluator |
| jep-langgraph-adapter | `140171170409` | [#6](https://github.com/hjs-spec/jep-langgraph-adapter/pull/6) | Framework observation with an unsigned archive; preserve graph hooks |
| jep-openai-agents-middleware | `7ef8147ef537` | [#5](https://github.com/hjs-spec/jep-openai-agents-middleware/pull/5) | Framework observation with an unsigned archive; preserve RunHooks |
| jep-mcp-wrapper | `d60ba4962e91` | [#5](https://github.com/hjs-spec/jep-mcp-wrapper/pull/5) | Separate unsigned MCP archive; preserve nested replay |
| jep-claude-replay | `c9803b5abf11` | [#5](https://github.com/hjs-spec/jep-claude-replay/pull/5) | Separate Claude importer, signatures and `.jcrpack` |

The earlier archives remain `jep-architecture`, `jep-vs-logging` and
`jep-e2e-demo`. Their documentation destinations are listed in [PROJECTS.md](PROJECTS.md).

## Evidence and limits

At the audit, the eight targets each had zero stars, forks and open issues/PRs.
GitHub release assets showed zero to four downloads per asset. These are limited
signals: they do not establish the absence of external consumers or package-registry
downloads.

Inspection of the current primary implementations found no imports of these eight
packages. Remaining references were principally documentation and historical
compatibility/demo material. The decision therefore reduces separate maintenance
without deleting compatibility readers. It is reversible by unarchiving a repository.

The Agent SDK does **not** already implement every retired feature. Its
[integration guide](https://github.com/hjs-spec/jep-agent-sdk/blob/main/docs/INTEGRATIONS.md)
names each gap, the original reader and the supported signed recording/report path.
No automatic conversion is promised; original signed artifacts must remain intact.
Any future bridge must define source format, mapping, preserved evidence and tests.

## Maintained ownership

- Core owns protocol rules, schemas, conformance vectors and validators.
- Quickstart owns the first runnable signed-event workflow.
- API owns shared signing, verification, storage and acceptance state.
- Python/JavaScript/Go HTTP clients and CLI own transport and language interfaces.
- Agent SDK owns local signed recording, verification and reports.
- Companion protocols and independent formats keep their explicit boundaries.

[Core #29](https://github.com/hjs-spec/jep-core/pull/29) records the architecture
boundary. [Agent SDK #12](https://github.com/hjs-spec/jep-agent-sdk/pull/12) documents
supported integration and capability gaps. The organization homepage retains only
three starting points: protocol, Quickstart and integration.

The GitHub About descriptions of Core, API, Python/JavaScript/Go clients, CLI,
Agent SDK and Quickstart now match their current Core 0.7 interfaces.

Reopening an experiment requires a concrete consumer, a named format and a
maintenance owner. Add capabilities to their existing owner before adding a repository.

## Validation and delivery

The existing CI workflows passed for all ten component PRs before merge. The
Agent SDK guide's signed example was also executed: two J events were written and
their chain verified. Changes were documentation and one adapter docstring; runtime
behavior, published package versions and commands were unchanged.

All eight repositories were confirmed archived after the notices were merged.
This step does not resolve the registry/deployment configuration blockers recorded
in [DELIVERY-2026-09-26.md](DELIVERY-2026-09-26.md), and introduces no new software
release.
