---
name: ardians-product-launch
description: Validates, reviews, and releases a product through QA, code review, CI, and deployment. Use when the user asks to ship this MVP, prepare a release, QA and release, run the release checklist, or deploy the product.
triggers:
- ship this mvp
- prepare a release
- qa and release
- release checklist
- deploy the product
---

# Ardians Product Launch

Stage 6 of the Ardians product pipeline. Prove the build works, review it,
release it, and land it on a deploy target.

## Entry and exit

- **Entry:** code on an isolated branch with a green test suite.
- **Exit:** a release with notes and a named deploy target.

Read `../ardians-product-orchestrator/references/pipeline.md` for stage order
and the gate rule.

## Steps

1. **Run functional QA.** Invoke `qa-changes` to exercise the changed behavior
   on the real code paths. Record the environment, the steps, and the observed
   results. Do not substitute reading the diff for running it.
2. **Review the change.** Invoke `code-review` for material correctness,
   security, compatibility, and maintainability risks. Use
   `requesting-code-review` to frame the review and `receiving-code-review` to
   weigh the feedback before acting on it.
3. **Drive CI to green.** Invoke `github-actions` for pipeline changes and
   `iterate` to take a pull request through CI, review, and QA until it is
   merge-ready. A red required check blocks the release.
4. **Write the notes.** Invoke `release-notes` to turn history since the last
   release into breaking changes, features, and fixes.
5. **Integrate the branch.** Invoke `finishing-a-development-branch` to decide
   how the work lands. Merging, pushing to a shared branch, and publishing are
   side effects: confirm with the user before any of them.
6. **Deploy.** Use `vercel` for hosted apps and `docker` for container targets.
   Deploy to a preview or staging target first unless the user explicitly asks
   for production.

## Gate

Stop after QA and review pass and the release candidate is ready. Present the QA
result, review outcome, CI status, and deploy target, then ask the user to
approve the merge and deploy. Do not merge or deploy without explicit
confirmation.

## Completion contract

Do not declare launched from a plan. The QA run, the review outcome, and the CI
result must have executed in this session, and the deploy target must be named.
