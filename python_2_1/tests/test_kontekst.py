import io
from contextlib import redirect_stdout

import pytest

from kontekst import Logger, FileWriter, SafeDivision


def test_logger_prints_enter_and_exit():
    buf = io.StringIO()
    with redirect_stdout(buf):
        with Logger():
            pass
    output = buf.getvalue()
    assert "Start sekcji logowania" in output
    assert "Koniec sekcji logowania" in output


def test_file_writer_writes_text(tmp_path):
    path = tmp_path / "out.txt"
    with FileWriter(str(path)) as f:
        f.write("test\n")
    assert path.read_text() == "test\n"


def test_file_writer_closes_on_exception(tmp_path):
    path = tmp_path / "out.txt"
    with pytest.raises(ValueError):
        with FileWriter(str(path)) as f:
            f.write("data\n")
            raise ValueError("boom")
    assert f.closed
    assert path.read_text() == "data\n"


def test_file_writer_does_not_suppress_exception():
    with pytest.raises(RuntimeError):
        with FileWriter("unused.txt"):
            raise RuntimeError("propagated")


def test_safe_division():
    with SafeDivision() as sd:
        assert sd.divide(10, 2) == 5.0


def test_safe_division_suppresses_zero_division(capsys):
    result = None
    with SafeDivision() as sd:
        result = sd.divide(5, 0)
    assert result is None
    assert "Nie można dzielić przez zero" in capsys.readouterr().out


def test_safe_division_does_not_suppress_other_errors():
    with pytest.raises(TypeError):
        with SafeDivision():
            raise TypeError("not suppressed")
