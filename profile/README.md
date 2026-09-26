# JEP · Judgment Event Protocol

Signed statements of **Judgment (J), Delegation (D), Termination (T), and Verification (V)**.

The current protocol is **JEP Core 0.7**, wire major `jep: "1"`. Software package versions are independent of the protocol version.

## Start here

| Goal | Canonical entry |
|---|---|
| Read the protocol or run conformance checks | [jep-core](https://github.com/hjs-spec/jep-core) |
| Run a signed tool call and replay it locally | [jep-quickstart](https://github.com/hjs-spec/jep-quickstart) |
| Connect an application | [Python](https://github.com/hjs-spec/sdk-py) · [JavaScript](https://github.com/hjs-spec/sdk-js) · [Go](https://github.com/hjs-spec/sdk-go) · [API](https://github.com/hjs-spec/jep-api) · [CLI](https://github.com/hjs-spec/cli) |
| Add agent recording and reports | [jep-agent-sdk](https://github.com/hjs-spec/jep-agent-sdk) |

Core 0.7 uses Event Identity `(who,id)` for stable identity and Event Hash for an exact signed artifact. Validation reports independent checks and `valid`, `invalid`, or `indeterminate`. A valid signature does not establish truth, authority, legal effect, causality, or complete logging.

The published Internet-Draft -07 is frozen. Historical formats are read through explicit compatibility paths; failed current validation never selects a legacy decoder automatically.

## Find the rest

[Project directory](https://github.com/hjs-spec/.github/blob/main/PROJECTS.md) lists companion implementations, integrations, visual tools, research and historical baselines. [Architecture](https://github.com/hjs-spec/jep-architecture) explains their boundaries.

[HJS](https://github.com/hjs-spec/hjs-05) covers archive/evidence lifecycle; [JAC](https://github.com/hjs-spec/jac-agent-02) covers declared dependency chains. They are optional companion work, not sequential Core authorization gates.

Use each repository's **Releases** page for immutable downloads and its Actions page for the tested revision. A source release, package-registry upload, container image and live deployment are distinct delivery results; a hosted demo may lag the source.

[Verified delivery status — 2026-09-26](https://github.com/hjs-spec/.github/blob/main/DELIVERY-2026-09-26.md) lists published versions, downloads and remaining registry/deployment configuration.
