# Playbook

My operating rules for study, investing and exercise. Each area has one file. The top of each file is the current rules and nothing else. Reasons, evidence and history are collapsed underneath.

## Layout

```
study/playbook.md
investing/playbook.md
exercise/playbook.md
scripts/check_reviews.py        lists rules past their review date
.github/                        PR template, idea template, monthly review workflow
setup.sh                        one-off: create the private GitHub repo and labels
```

## How it works

1. **Rules** are short instructions I can act on without thinking.
2. **Detail** is one collapsed block per rule: why, evidence, change trigger, review date.
3. **Changelog** is one collapsed block per file, one line per change.
4. **Ideas** are GitHub Issues with the `idea` label. They never touch a playbook directly.
5. **Changes** to a rule happen only through a pull request. The PR template forces a reason, the trigger that justifies the change, and a changelog line.
6. **Monthly review**: a workflow opens an issue on the 1st listing overdue rules and open ideas. That is the only time ideas get promoted to rules.

## Changing a rule

1. Capture the idea as an issue (label `idea`). Stop there.
2. At review, check the rule's change trigger. If it is not met, close the idea or leave it.
3. If it is met, branch, edit the rule, update its detail block, bump the review date, add a changelog row.
4. Open a PR using the template. Merge it.

## Phone

- **Read**: the GitHub mobile app renders the markdown and the collapsible blocks. Pin the repo, or bookmark each playbook file.
- **Capture ideas**: create an issue from the app (New issue, pick the Idea template).
- **Edit**: open the repo in a mobile browser and press `.` on desktop, or go to `github.dev/<user>/playbook`, for a full editor. On iOS, Working Copy is the alternative.
- **Notifications**: turn on issue notifications in the app so the monthly review reaches you.

## Setup

```
gh auth login
./setup.sh playbook
```

Then replace the example rules in each playbook with your own.
