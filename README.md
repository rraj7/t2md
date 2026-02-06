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
    Uses OpenAI models to convert raw transcripts into:

    -   Executive summaries

    -   Textbook-style prose with clear structure

-   🧩 **Configurable prompt ingestion**

    -   Use a bundled default prompt

    -   Or pass your own Markdown prompt file to fully control output style and structure

-   📄 **Multiple output formats**

    -   Markdown (`.md`)

    -   Word documents (`.docx`) with proper headings and lists\
        (DOCX can be exported to PDF using Word or Google Docs)

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

`brew install pipx
pipx ensurepath
pipx install git+https://github.com/rraj7/t2md.git`

Verify installation:

`t2md --help
t2md doctor`

* * * * *

Setup (One-time)
----------------

Add your OpenAI API key to your shell config:

`export OPENAI_API_KEY="sk-..."`

Reload your shell:

`source ~/.zshrc`

* * * * *

Usage
-----

Basic usage:

`t2md run /path/to/transcripts/module_03`

Specify output format:

`t2md run /path/to/transcripts/module_03 --format docx`

Use a custom prompt file:

`t2md run /path/to/transcripts/module_03\
  --prompt /path/to/prompt_rules.md`

Specify output directory:

`t2md run /path/to/transcripts/module_03\
  --out ~/Documents/t2md_outputs`

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

