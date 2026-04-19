# t2md

[![CI](https://github.com/rraj7/t2md/actions/workflows/ci.yml/badge.svg)](https://github.com/rraj7/t2md/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/t2md?color=blue&label=PyPI)](https://pypi.org/project/t2md/)
[![Python](https://img.shields.io/pypi/pyversions/t2md?color=blue)](https://pypi.org/project/t2md/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Turn raw transcripts into study-ready reading.**

`t2md` is a command-line tool that takes a folder of transcripts (lecture captions, interview notes, Zoom dumps) and runs them through an LLM to produce a clean executive summary plus textbook-style prose. It auto-picks a cheap model for short inputs and a stronger one for long inputs, and it works with either OpenAI or Anthropic.

Why not just paste into ChatGPT? `t2md` handles batches of files, concatenates multi-part transcripts, picks the right model for the input size so you don't overpay, and writes consistent Markdown / DOCX / LaTeX you can commit, diff, and re-run on updated source.

---

## What it does

**Input** — raw transcript (`examples/mit6_7960_lec01_intro_deep_learning/mit6_7960f24_lec01.txt`):

```text
MITOCW | mit6_7960f24_lec01.mp4
[SQUEAKING]
[RUSTLING]

SARA BEERY:
So why are we all here? Deep learning has clearly been exploding in society. Machine learning
generally is something that, when I started studying it about 13 years ago, didn't work, and
now it works. So how many of you here in this room used AI in the last week?
Yeah, almost everybody, probably everybody...
```

**Output** — generated markdown ([full file](examples/sample_outputs/lec01_intro_deep_learning.md)):

```markdown
# Executive Summary
- Thesis: Deep learning has rapidly evolved to become a transformative technology...
- Key Concepts: neural networks, differential programming, activation functions...
- What to Remember: ReLU is the default activation; transfer learning leverages...

# Reading
## Introduction to Deep Learning
Deep learning has gained significant traction over recent years...

## Historical Perspective on Neural Networks
The journey of neural networks is marked by cycles of enthusiasm and skepticism...
```

Two pre-generated samples are committed at [`examples/sample_outputs/`](examples/sample_outputs/) so you can see the output quality before running anything.

---

## Install

```bash
pipx install t2md
```

Or with plain pip:

```bash
pip install t2md
```

For PDF input support:

```bash
pipx install "t2md[pdf]"
```

If you want to install from source:

```bash
brew install pipx && pipx ensurepath
pipx install git+https://github.com/rraj7/t2md.git
```

Verify:

```bash
t2md --help
t2md doctor
```

## Setup

Export at least one API key:

```bash
export OPENAI_API_KEY="sk-..."          # or
export ANTHROPIC_API_KEY="sk-ant-..."
```

Reload your shell (`source ~/.zshrc`) and run `t2md doctor` to confirm.

---

## Usage

```bash
# Basic run — auto-selects model by input size, writes Markdown to ./outputs
t2md run examples/mit6_7960_lec01_intro_deep_learning

# Word document output (openable in Word, Google Docs, Pages)
t2md run /path/to/transcripts --format docx

# LaTeX output for PDF-ready workflows
t2md run /path/to/transcripts --format tex

# Use Claude instead of OpenAI
t2md run /path/to/transcripts --provider anthropic

# Override the auto-selected model
t2md run /path/to/transcripts --model gpt-4o

# Use a built-in prompt preset (lecture or interview)
t2md run /path/to/transcripts --preset lecture
t2md run /path/to/transcripts --preset interview

# Custom prompt file — full control over the output style
t2md run /path/to/transcripts --prompt /path/to/prompt_rules.md

# Custom output directory
t2md run /path/to/transcripts --out ~/Documents/t2md_outputs

# Raise the output cap if the generated file looks truncated
t2md run /path/to/transcripts --max-output-tokens 32000
```

### Automatic model selection

Without `--model`, `t2md` picks the cheapest model that can handle the input:

| Input tokens | OpenAI | Anthropic |
|---|---|---|
| < 4,000 | `gpt-4o-mini` | `claude-haiku-4-5` |
| 4,000 – 32,000 | `gpt-4o` | `claude-sonnet-4-6` |
| > 32,000 | `gpt-4o` + warning | `claude-sonnet-4-6` + warning |

A typical 60-minute lecture transcript (~15k tokens) runs through `gpt-4o` for roughly **$0.05–$0.10**. A short 10-minute clip on `gpt-4o-mini` is under a cent. Claude costs are in the same ballpark at the matching tier.

---

## Output

All transcripts in a folder are concatenated and summarized into a single output file named `<folder>_All.<ext>`. Each output contains:

1. **Executive Summary** — thesis, 5–10 key concepts, examples, what to remember
2. **Structured Reading** — textbook-style prose with TOC, headings, and a synthesis

For example, running on a folder named `module_03/` produces:

```text
outputs/
  module_03_All.md
  module_03_All.docx
  module_03_All.tex
```

---

## Design philosophy

- **Opinionated defaults, flexible overrides** — sensible output for zero config, full control when you need it
- **Prompt-first** — the transformation rules live in a Markdown file you can edit
- **Clean secret handling** — API keys come from environment variables, never commands or code
- **Extensible** — provider abstraction (see `src/t2md/providers.py`) makes it easy to add Ollama, Gemini, etc.

---

## Roadmap

Supported input formats today: `.txt`, `.md`, `.srt`, `.vtt`, `.pdf`, `.docx`.

- Local Ollama provider (scaffolding already in place)
- Additional prompt presets (meeting notes, research papers, book chapters)
- YouTube VTT / auto-caption ingestion
- CSV / PPTX input

---

## Contributing

Architecture is settled enough to use day-to-day but open enough that contributions can still shape direction. Issues, PRs, and ideas welcome — especially around new input formats and prompt presets.

## License

MIT. Example transcripts in `examples/` are MIT OCW content licensed under CC BY-NC-SA 4.0 — see [`examples/README.md`](examples/README.md) for attribution.
