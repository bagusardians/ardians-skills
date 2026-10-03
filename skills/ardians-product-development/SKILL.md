---
name: ardians-product-development
description: Implements a product on an isolated branch with tests. Use when the user asks to implement the product, build the MVP, start development, write the code, or execute the build tasks.
triggers:
- implement the product
- build the mvp
- start development
- write the code
- execute the build tasks
---

# Ardians Product Development

Stage 4 of the Ardians product pipeline. Implement the approved task breakdown
on an isolated branch, test first, and leave green tests behind.

## Entry and exit

- **Entry:** approved architecture and an ordered task breakdown.
- **Exit:** working code on an isolated branch with a passing test suite.

Read `../ardians-product-orchestrator/references/pipeline.md` for stage order
and parallelization points.

## Steps

1. **Isolate the work.** Invoke `using-git-worktrees` to create or verify an
   isolated workspace. Never implement on main or master without explicit
   consent. Choose the toolchain skill (`uv`, `npm`, or `deno`) from the stack
   and initialize the project with it.
2. **Execute the plan.** Invoke `executing-plans` when you are the single
   implementer. Follow the task breakdown in order. If you have a subagent tool
   and the tasks are independent, invoke `subagent-driven-development` instead.
3. **Test first.** Invoke `test-driven-development` for every task. Write the
   failing test, watch it fail, implement, watch it pass, then run the whole
   suite. A test that never failed proves nothing.
4. **Parallelize safely.** Use `dispatching-parallel-agents` for independent
   workstreams. Never let two workstreams write the same file or share a branch
   without isolation.
5. **Keep security in the loop.** Invoke `security` for authentication,
   authorization, input handling, secrets, and dependency choices as they come
   up, not as a final pass.
6. **Containerize when asked.** Use `docker` when the product needs a container
   or reproducible environment.

## Gate

Stop when the task breakdown is implemented and the suite is green. Report the
branch, the test command, and its result, then ask the user to approve before
stage 6 (launch). Do not run stage 5 or 6 unprompted.

## Completion contract

Do not claim the stage is done from the diff. The final suite run must have
executed in this session and its output read. If any task lacks a passing test,
the stage is not complete.
