t2md
====

`t2md` is an open-source, command-line tool for transforming unstructured learning content (such as video transcripts, lecture notes, or raw text files) into **clean, structured, study-ready documents** using LLMs.

The project sits at the intersection of **developer tooling**, **AI-assisted learning**, and **content engineering**. It is designed to be simple to use, easy to extend, and flexible enough to support multiple workflows and formats over time.

* * * * *

Why t2md?
---------

Most learning content today is:

-   scattered across files

-   conversational or unstructured

-   hard to reuse across formats (notes, docs, slides, etc.)

`t2md` solves this by providing a **repeatable transformation pipeline**:

-   input a folder of raw content

-   apply a configurable prompt

-   generate structured outputs that are actually readable and shareable

The goal is not just summarization, but **content transformation**.

* * * * *

Current Features
----------------

-   📁 **Folder-based input**\
    Process an entire directory of transcripts or text files in one command.

-   🧠 **LLM-driven transformation**\
    Works with OpenAI (GPT-4o family) or Anthropic (Claude family). Converts raw transcripts into:

    -   Executive summaries

    -   Textbook-style prose with clear structure

-   💸 **Auto model selection**\
    Picks the cheapest model that can handle your input size. Short lectures → `gpt-4o-mini` or `claude-haiku-4-5`. Longer content → `gpt-4o` or `claude-sonnet-4-6`. Override with `--model` any time.

-   🧩 **Configurable prompt ingestion**

    -   Use a bundled default prompt

    -   Or pass your own Markdown prompt file to fully control output style and structure

-   📄 **Multiple output formats**

    -   Markdown (`.md`)

    -   Word documents (`.docx`) with proper headings and lists\
        (DOCX can be exported to PDF using Word or Google Docs)
    -   LaTeX (`.tex`) documents for PDF-ready workflows

-   🧱 **Installable CLI**

    -   Install once

    -   Run from anywhere

    -   No Makefiles or local scripts required

-   🔐 **Clean secret handling**

    -   API keys are read from environment variables

    -   No keys in commands, code, or git history

* * * * *

Installation
------------

Recommended: `pipx` (isolated, clean installs)

```bash
brew install pipx
pipx ensurepath
pipx install git+https://github.com/rraj7/t2md.git
```

Verify installation:

```bash
t2md --help
t2md doctor
```

* * * * *

Setup (One-time)
----------------

`t2md` supports two LLM providers. Set at least one API key in your shell config:

```bash
# For OpenAI (default)
export OPENAI_API_KEY="sk-..."

# For Anthropic / Claude
export ANTHROPIC_API_KEY="sk-ant-..."
```

Reload your shell:

```bash
source ~/.zshrc
```

Run `t2md doctor` to confirm which providers are configured.

* * * * *

Usage
-----

### Try it with bundled examples

Two real MIT OpenCourseWare lecture transcripts ship in the repo, so you can try `t2md` without supplying your own data:

```bash
t2md run examples/mit6_7960_lec01_intro_deep_learning
t2md run examples/mit6_7960_lec02_training_neural_networks --format docx
```

See [`examples/README.md`](examples/README.md) for attribution.

### Common commands

```bash
# Basic run (auto-selects the cheapest model that can handle the input)
t2md run /path/to/transcripts/module_03

# Word document output
t2md run /path/to/transcripts/module_03 --format docx

# LaTeX output
t2md run /path/to/transcripts/module_03 --format tex

# Use Claude instead of OpenAI
t2md run /path/to/transcripts/module_03 --provider anthropic

# Override the auto-selected model
t2md run /path/to/transcripts/module_03 --model gpt-4o

# Custom prompt file
t2md run /path/to/transcripts/module_03 --prompt /path/to/prompt_rules.md

# Custom output directory
t2md run /path/to/transcripts/module_03 --out ~/Documents/t2md_outputs
```

### Automatic model selection

When you don't pass `--model`, `t2md` picks one based on the token count of your input:

| Tokens | OpenAI | Anthropic |
|---|---|---|
| < 4,000 | `gpt-4o-mini` | `claude-haiku-4-5` |
| 4,000 – 32,000 | `gpt-4o` | `claude-sonnet-4-6` |
| > 32,000 | `gpt-4o` + warning | `claude-sonnet-4-6` + warning |

Short lectures cost fractions of a cent; longer dense content gets the stronger model automatically.

* * * * *

Output
------

By default, `t2md` generates a single file per run containing:

1.  **Executive Summary**

    -   Core thesis

    -   Key concepts

    -   Examples or case studies

    -   "What to remember" section

2.  **Structured Reading**

    -   Textbook-style prose

    -   Logical headings and sections

    -   Clean formatting

    -   End-of-document synthesis summary

Example output:

`outputs/
  module_03_All.md
  module_03_All.docx`

* * * * *

Design Philosophy
-----------------

-   **Opinionated defaults, flexible overrides**

-   **Prompt-first architecture**

-   **Minimal setup for end users**

-   **Extensible for contributors**

-   **No heavy conversion engines required**

This project intentionally avoids over-engineering while keeping the core architecture open for growth.

* * * * *

Roadmap (Planned & Exploratory)
-------------------------------

`t2md` is intentionally early-stage, with room for contributors to shape its direction. Planned ideas include:

-   📥 **Multi-format input support**

    -   PDF, DOCX, CSV, TXT, MD, and more

-   📤 **Expanded output targets**

    -   PDF (via lightweight converters)

    -   LaTeX

    -   Kindle / e-reader optimized formats

    -   reMarkable-friendly outputs

    -   Presentation formats (PPT)

-   🔌 **Pluggable conversion backends**

    -   CloudConvert API

    -   Other public or local conversion engines

-   🧠 **Prompt modularization**

    -   Prompt selection per subject or topic

    -   Prompt composition pipelines

    -   LLM-assisted prompt generation

-   🖼️ **Multimodal workflows**

    -   Image inputs (slides, diagrams)

    -   Visual outputs (PNG, JPG)

-   💻 **Cross-platform binaries**

    -   macOS, Windows, Linux executables

* * * * *

Contributing
------------

This project is early enough that:

-   core architectural decisions are still open

-   contributions can meaningfully shape direction

...but mature enough to be:

-   immediately usable

-   practical

-   grounded in real workflows

If you're interested in developer tooling, AI-assisted learning, or content engineering, contributions and ideas are very welcome.

* * * * *
