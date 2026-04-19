# Contributing to t2md

Thanks for your interest. The project is early-stage — architecture is stable enough to build on, but open enough that contributions can still shape direction meaningfully.

## Where to start

The most useful areas right now:

- **New input formats** — PDF and DOCX are just merged; other formats like `.csv`, `.pptx`, or YouTube VTT subtitles would be valuable additions
- **New prompt presets** — `prompts/lecture.md` and `prompts/interview.md` are the current built-ins; meeting notes, research papers, or book chapters would be natural additions
- **Ollama provider** — scaffolding is in `src/t2md/providers.py`; just needs `complete()` implemented using the Ollama Python client
- **Bug reports** — open an issue with the input type, command you ran, and the error

## Setup

```bash
git clone https://github.com/rraj7/t2md.git
cd t2md
pip install -e ".[dev]"        # installs the package + test/build tools
pip install -e ".[dev,pdf]"    # also includes pdfplumber for PDF input
```

Run the test suite:

```bash
pytest
```

Check the CLI loads:

```bash
t2md --help
t2md doctor
```

## Project layout

```text
src/t2md/
  cli.py              # all CLI commands (run, doctor)
  providers.py        # LLM provider abstraction (OpenAI, Anthropic, Ollama stub)
  default_prompt.md   # default transformation rules
  prompts/            # built-in prompt presets
    lecture.md
    interview.md

tests/
  test_providers.py
  test_file_readers.py
  test_sort_key.py
  test_latex_conversion.py
```

## Adding a new provider

1. Add a class to `src/t2md/providers.py` that extends `Provider`
2. Implement `complete(self, prompt, model, max_output_tokens) -> tuple[str, bool]`
3. Register it in the `PROVIDERS` dict
4. Add tests in `tests/test_providers.py` (mock the SDK client, don't hit the real API)

## Adding a new prompt preset

1. Create a Markdown file in `src/t2md/prompts/`
2. Add an entry to the `PRESETS` dict in `src/t2md/cli.py`
3. No tests required — just make sure `t2md run <folder> --preset <name>` works end-to-end

## Pull requests

- Keep PRs focused — one feature or fix per PR
- Add tests for new behaviour; don't break existing ones (`pytest` must stay green)
- Update `CHANGELOG.md` under `[Unreleased]` with a short entry
- The CI matrix runs Python 3.10–3.13; please don't use syntax only available in newer versions

## Code style

No linter is enforced yet, but the codebase follows these conventions:
- No unnecessary comments (well-named identifiers are enough)
- No backwards-compatibility shims — change the code directly
- Validate at system boundaries (CLI flags, file I/O), trust internal invariants
