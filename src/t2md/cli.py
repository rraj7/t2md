from __future__ import annotations

import os
import re
from pathlib import Path
from importlib.resources import files as pkg_files

import typer
from openai import OpenAI
from rich import print
from rich.console import Console

app = typer.Typer(no_args_is_help=True)
console = Console()

NUM = re.compile(r"(\d+)(?:\.(\d+))?(?:\.(\d+))?")

SUPPORTED_EXTS = {".txt", ".md", ".srt", ".vtt"}

def sort_key(p: Path):
    """
    Prefer numeric ordering in filenames like 3.7.1, 3.7.2, etc.
    Fall back to modified time (older first) when no numeric pattern exists.
    """
    m = NUM.search(p.stem)
    if m:
        parts = tuple(int(x) if x else -1 for x in m.groups())
        return (0, parts, p.name.lower())
    return (1, p.stat().st_mtime, p.name.lower())

def list_transcripts(folder: Path) -> list[Path]:
    files = [p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS]
    files.sort(key=sort_key)
    return files

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore").strip()

def load_default_prompt() -> str:
    # Bundled file inside the installed package
    prompt_path = pkg_files("t2md").joinpath("default_prompt.md")
    return prompt_path.read_text(encoding="utf-8").strip()

def derive_module_name(folder: Path) -> str:
    # Use folder name by default (e.g., module_03 -> module_03)
    return folder.name

@app.command("run")
def run(
    folder: Path = typer.Argument(..., help="Folder containing transcript files"),
    module: str | None = typer.Option(None, "--module", help="Module name (default: folder name)"),
    out: Path = typer.Option(Path("./outputs"), "--out", help="Output directory"),
    prompt: Path | None = typer.Option(None, "--prompt", help="Optional prompt markdown file override"),
    model: str = typer.Option("gpt-4.1-mini", "--model", help="Model to use"),
):
    """
    Generate a combined Markdown file containing:
      1) Executive Summary
      2) Textbook-style Reading
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise typer.BadParameter(
            "OPENAI_API_KEY is not set. Add it to ~/.zshrc (recommended) or export it in your shell."
        )

    folder = folder.expanduser().resolve()
    out = out.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    if not folder.exists():
        raise typer.BadParameter(f"Folder not found: {folder}")

    module_name = module or derive_module_name(folder)

    prompt_rules = ""
    if prompt:
        prompt_path = prompt.expanduser().resolve()
        if not prompt_path.exists():
            raise typer.BadParameter(f"Prompt file not found: {prompt_path}")
        prompt_rules = read_text(prompt_path)
    else:
        prompt_rules = load_default_prompt()

    files = list_transcripts(folder)
    if not files:
        raise typer.BadParameter("No transcript files found (.txt/.md/.srt/.vtt).")

    combined = []
    for f in files:
        combined.append(f"\n\n---\n\n## SOURCE FILE: {f.name}\n\n{read_text(f)}\n")
    transcripts = "".join(combined).strip()

    user_prompt = f"""
You will be given:
1) PROMPT_RULES (how to transform)
2) TRANSCRIPTS (raw content)

Return EXACTLY two top-level Markdown sections:

# {module_name} — Executive Summary
- thesis (2–4 sentences)
- 5–10 key concepts
- 2–5 examples/case studies
- what to remember (3–7 bullets)

# {module_name} — Reading
Follow PROMPT_RULES to create a readable textbook-style markdown:
- include a TOC
- clean headings
- preserve important examples
- remove transcript artifacts
- end with a synthesis summary

PROMPT_RULES:
{prompt_rules}

TRANSCRIPTS:
{transcripts}
""".strip()

    client = OpenAI(api_key=api_key)

    with console.status("Generating markdown..."):
        resp = client.responses.create(model=model, input=user_prompt)
        output = resp.output_text.strip()

    out_file = out / f"{module_name}_All.md"
    out_file.write_text(output, encoding="utf-8")

    print("[cyan]Processed files (in order):[/cyan]")
    for f in files:
        print(f"  - {f.name}")
    print(f"\n[green]Wrote:[/green] {out_file}")

@app.command("doctor")
def doctor():
    """Quick sanity checks."""
    ok = True
    if not os.getenv("OPENAI_API_KEY"):
        ok = False
        print("[red]Missing:[/red] OPENAI_API_KEY environment variable")
    else:
        print("[green]OK:[/green] OPENAI_API_KEY is set")

    if ok:
        print("[green]All good.[/green]")
    else:
        raise typer.Exit(code=1)
