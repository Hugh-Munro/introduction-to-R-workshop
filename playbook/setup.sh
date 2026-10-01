#!/usr/bin/env bash
# One-off setup: create a private GitHub repo from this folder and add labels.
# Requires git and the GitHub CLI (gh), authenticated with `gh auth login`.
set -euo pipefail

REPO_NAME="${1:-playbook}"

cd "$(dirname "$0")"

if [ ! -d .git ]; then
  git init -b main
fi

git add .
git commit -m "Initial playbook"

gh repo create "$REPO_NAME" --private --source=. --remote=origin --push

gh label create idea --description "Unvetted idea, handled at monthly review" --color 0E8A16 || true
gh label create review --description "Monthly review" --color 1D76DB || true

echo "Done. Repo: $(gh repo view --json url --jq .url)"
