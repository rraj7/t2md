from pathlib import Path
from unittest.mock import patch

from t2md.cli import sort_key


def _make(p: str):
    """Build a Path and stub .stat() so sort_key works without real files."""
    path = Path(p)
    fake_stat = type("S", (), {"st_mtime": 0})()
    with patch.object(Path, "stat", return_value=fake_stat):
        yield path


def test_numeric_ordering_prefers_semver_style(tmp_path):
    names = ["3.7.2_b.txt", "3.7.1_a.txt", "3.7.10_c.txt"]
    paths = [tmp_path / n for n in names]
    for p in paths:
        p.touch()
    ordered = sorted(paths, key=sort_key)
    assert [p.name for p in ordered] == ["3.7.1_a.txt", "3.7.2_b.txt", "3.7.10_c.txt"]


def test_numeric_files_sort_before_non_numeric(tmp_path):
    numeric = tmp_path / "1.1_lecture.txt"
    non_numeric = tmp_path / "zzz_appendix.txt"
    numeric.touch()
    non_numeric.touch()
    ordered = sorted([non_numeric, numeric], key=sort_key)
    assert ordered[0] == numeric


def test_non_numeric_falls_back_to_name_order(tmp_path):
    a = tmp_path / "apple.txt"
    b = tmp_path / "banana.txt"
    a.touch()
    b.touch()
    ordered = sorted([b, a], key=sort_key)
    assert [p.name for p in ordered] == ["apple.txt", "banana.txt"]
