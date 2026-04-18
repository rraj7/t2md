from t2md.cli import escape_latex, write_latex_from_markdown


def test_escape_latex_handles_special_chars():
    assert escape_latex("50% & rising $USD") == r"50\% \& rising \$USD"


def test_escape_latex_preserves_plain_text():
    assert escape_latex("hello world") == "hello world"


def test_latex_output_includes_preamble_and_document(tmp_path):
    out = tmp_path / "out.tex"
    write_latex_from_markdown("# Title\n\nSome text.", out, "Demo")
    text = out.read_text()
    assert r"\documentclass" in text
    assert r"\begin{document}" in text
    assert r"\end{document}" in text
    assert r"\section{Title}" in text
    assert r"\title{Demo}" in text


def test_latex_converts_bullet_lists(tmp_path):
    out = tmp_path / "list.tex"
    write_latex_from_markdown("- apple\n- banana", out, "L")
    text = out.read_text()
    assert r"\begin{itemize}" in text
    assert r"\item apple" in text
    assert r"\item banana" in text
    assert r"\end{itemize}" in text


def test_latex_converts_code_blocks_to_verbatim(tmp_path):
    out = tmp_path / "code.tex"
    write_latex_from_markdown("```\nprint('hi')\n```", out, "C")
    text = out.read_text()
    assert r"\begin{verbatim}" in text
    assert "print('hi')" in text
    assert r"\end{verbatim}" in text
