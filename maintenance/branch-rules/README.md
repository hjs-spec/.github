# Main-branch rules

All eight rulesets below were activated and verified on **2026-10-01**. GitHub
reports `enforcement: active` and `protected: true` for every `main` branch. The
24 required check names, GitHub Actions source and configured parameters match
these JSON files; bypass lists are empty.

Editing these files alone does not change GitHub settings. Update the live
ruleset as part of any later configuration change.

Each configuration requires a pull request, resolved review threads, an
up-to-date branch and the listed GitHub Actions checks. It blocks force pushes
and deletion of `main`, with no bypass actors. The approval count is zero so a
single maintainer can merge a tested pull request. This enforces PR and CI use;
it does not establish independent human review.

| Repository | Active ruleset | Required checks |
| --- | --- | --- |
| [jep-core](jep-core.json) | [24286888](https://github.com/hjs-spec/jep-core/rules/24286888) | Python 3.10–3.13; legacy 0.6 TypeScript on Node 20/22, Go and cross-language checks; installed wheel on Linux/Windows/macOS; signed artifacts |
| [jep-agent-sdk](jep-agent-sdk.json) | [24286923](https://github.com/hjs-spec/jep-agent-sdk/rules/24286923) | Python 3.10–3.13; viewer container; package coexistence |
| [jep-api](jep-api.json) | [24286950](https://github.com/hjs-spec/jep-api/rules/24286950) | `test` (includes PostgreSQL and source-license checks) |
| [jep-quickstart](jep-quickstart.json) | [24286958](https://github.com/hjs-spec/jep-quickstart/rules/24286958) | `test` (includes real HTTP and distribution-license checks) |
| [sdk-py](sdk-py.json) | [24286975](https://github.com/hjs-spec/sdk-py/rules/24286975) | `python-tests` (includes distribution-license checks) |
| [sdk-js](sdk-js.json) | [24286995](https://github.com/hjs-spec/sdk-js/rules/24286995) | `node-tests` |
| [sdk-go](sdk-go.json) | [24287012](https://github.com/hjs-spec/sdk-go/rules/24287012) | `go-tests` |
| [cli](cli.json) | [24287036](https://github.com/hjs-spec/cli/rules/24287036) | `python-tests` |

Exact check names and GitHub Actions app ID `15368` were verified against current
workflow runs on 2026-10-01. Each required job runs for every pull request. Release,
package publication, and path-filtered jobs are excluded because they do not run
on every PR. If workflows or job names change, update the active rules and these
files together before merging the rename.

## Maintain and verify

Use a repository administrator account. Review the current rules and inherited
rules before changing them; keep the active rules and these files aligned.
In GitHub, open **Settings → Rulesets** and edit the existing named ruleset.

For an administrator using the GitHub CLI, from this directory:

```sh
repo=jep-api
ruleset_id=24286950  # use the matching ID from the table

gh api "repos/hjs-spec/$repo/rulesets?includes_parents=true"
gh api "repos/hjs-spec/$repo/rulesets/$ruleset_id"
# After reviewing the intended change:
gh api --method PUT "repos/hjs-spec/$repo/rulesets/$ruleset_id" --input "$repo.json"
gh api "repos/hjs-spec/$repo/rules/branches/main"
gh api "repos/hjs-spec/$repo/branches/main" --jq .protected
```

The active branch rules must contain the four configured rule types, exact check
contexts and strict status checking. Confirm required checks on a normal PR;
do not test by attempting a force push or deletion. Record subsequent activation
or verification changes in the [current delivery status](../../DELIVERY-CURRENT.md).

See GitHub's [rules API](https://docs.github.com/en/rest/repos/rules) and
[ruleset management guide](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository).
