# Contributing to t2md

Thanks for contributing.

## Workflow

1. Create a feature branch from `main`.
2. Make focused changes.
3. Open a pull request to `main`.
4. Get at least one approval.
5. Merge after required checks pass.

## Branch Naming

Use lowercase branch names with this pattern:

- `feature/<scope>-<short-description>`
- `fix/<scope>-<short-description>`
- `chore/<scope>-<short-description>`
- `docs/<scope>-<short-description>`
- `refactor/<scope>-<short-description>`
- `release/<version>`

Examples:

- `feature/auto-chunking-pipeline`
- `fix/latex-inline-escape`
- `release/v0.2.0`

## Commit Messages

Use short conventional commit prefixes:

- `feat: ...`
- `fix: ...`
- `docs: ...`
- `chore: ...`
- `refactor: ...`
- `test: ...`

## Local Setup

1. Install in editable mode:
   `pip install -e .`
2. Set environment variable:
   `export OPENAI_API_KEY="sk-..."`
3. Verify CLI:
   `t2md --help`
   `t2md doctor`

## Pull Request Expectations

- Keep PRs focused and small enough to review.
- Add or update docs when behavior changes.
- Run local checks before opening PR.
- Include what changed, why it changed, and how it was tested.
- Never commit secrets, API keys, or generated credentials.
