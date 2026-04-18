# Changelog

All notable changes to this project will be documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] — 2026-04-18

### Added
- **Anthropic/Claude provider support** via `--provider anthropic`. Auto-routes to `claude-haiku-4-5` for short inputs and `claude-sonnet-4-6` for longer ones.
- **Automatic model selection** based on prompt token count. Short inputs get cheaper models (`gpt-4o-mini` / `claude-haiku-4-5`), longer inputs get stronger models (`gpt-4o` / `claude-sonnet-4-6`). Override with `--model`.
- **Provider abstraction** (`src/t2md/providers.py`) — clean extension point for additional providers. Ollama scaffolding is in place for v0.3.
- **Example transcripts** — two real MIT OpenCourseWare lectures in `examples/` so the tool can be tried without sourcing your own data. Credit: MIT 6.7960 Fall 2024, Sara Beery, CC BY-NC-SA 4.0.
- **Test suite** — 18 smoke tests covering file sorting, provider routing, LaTeX conversion, and mocked SDK calls.
- **GitHub Actions CI** — runs on Python 3.10, 3.11, 3.12, 3.13.
- `tiktoken` dependency for accurate token counting.

### Changed
- **`t2md doctor`** now reports status for every registered provider, not just OpenAI.
- **Default model** is now selected dynamically; `--model` is an override rather than a hardcoded default.
- **Error handling** around API calls now catches network, auth, and rate-limit errors with a friendly message instead of a traceback.
- Bumped minimum Python version to 3.10 (from 3.9) to align with CI matrix and modern type-hint syntax.

### Fixed
- **Critical:** replaced broken `client.responses.create(input=...)` call (not a real method on the OpenAI SDK) with `client.chat.completions.create(messages=[...])`.
- **Critical:** replaced invalid default model `gpt-4.1-mini` (does not exist) with `gpt-4o-mini`.

## [0.1.0] — Initial release
- Folder-based transcript ingestion, configurable prompt, OpenAI-only, three output formats (md/docx/tex).
