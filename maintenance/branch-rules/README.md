# Main-branch rule configurations

These are reviewed GitHub ruleset inputs for the eight primary JEP repositories.
Committing these files does **not** activate GitHub settings. Check the live
rules API below before describing a repository as protected.

Each configuration requires a pull request, resolved review threads, an
up-to-date branch and the listed GitHub Actions checks. It blocks force pushes
and deletion of `main`, with no bypass actors. The approval count is zero so a
single maintainer can merge a tested pull request. This enforces PR and CI use;
it does not establish independent human review.

| Repository | Required checks |
| --- | --- |
| [jep-core](jep-core.json) | Python 3.10–3.13; legacy 0.6 TypeScript on Node 20/22, Go and cross-language checks; installed wheel on Linux/Windows/macOS; signed artifacts |
| [jep-agent-sdk](jep-agent-sdk.json) | Python 3.10–3.13; viewer container; package coexistence |
| [jep-api](jep-api.json) | `test` (includes PostgreSQL and source-license checks) |
| [jep-quickstart](jep-quickstart.json) | `test` (includes real HTTP and distribution-license checks) |
| [sdk-py](sdk-py.json) | `python-tests` (includes distribution-license checks) |
| [sdk-js](sdk-js.json) | `node-tests` |
| [sdk-go](sdk-go.json) | `go-tests` |
| [cli](cli.json) | `python-tests` |

Exact check names and GitHub Actions app ID `15368` were verified against current
workflow runs on 2026-10-01. Each required job runs for every pull request. Release,
package publication, and path-filtered jobs are excluded because they do not run
on every PR. If workflows or job names change, update the active rules and these
files together before merging the rename.

## Apply and verify

Use a repository administrator account. Review existing repository and inherited
rules first; do not create a duplicate or replace unrelated rules. The files can
be imported through **Settings → Rules → Rulesets → New ruleset → Import a
ruleset**. Confirm `main`, the required checks and **Active**, then save.

For an administrator using the GitHub CLI, from this directory and after checking
that the named ruleset does not already exist:

```sh
repo=jep-api  # choose one repository from the table

gh api "repos/hjs-spec/$repo/rulesets?includes_parents=true"
gh api --method POST "repos/hjs-spec/$repo/rulesets" --input "$repo.json"
gh api "repos/hjs-spec/$repo/rules/branches/main"
```

If a matching ruleset already exists, review it and update its ruleset ID instead
of posting a second one. The final GET must return the four active rule types,
with the exact check contexts and strict status checking. Open a normal PR and
confirm required checks appear before merging; do not test by attempting a force
push or deletion. Record the saved ruleset ID and verification date in the
[current delivery status](../../DELIVERY-CURRENT.md).

See GitHub's [rules API](https://docs.github.com/en/rest/repos/rules) and
[ruleset management guide](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository).
