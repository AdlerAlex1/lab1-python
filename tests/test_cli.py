import subprocess
import sys


def run_cli(*args):
    """Хелпер: запускает CLI и возвращает CompletedProcess."""
    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
        check =False,
    )


def test_cli_calc_success():
    result = run_cli("calc", "2 + 2")
    assert result.returncode == 0
    assert "4.0" in result.stdout


def test_cli_calc_error_exit_code():
    result = run_cli("calc", "2 +")
    assert result.returncode == 2
    assert "Ошибка" in result.stderr


def test_cli_convert_success():
    result = run_cli("convert", "1", "--from", "m", "--to", "cm")
    assert result.returncode == 0
    assert "100.0" in result.stdout


def test_cli_help():
    result = run_cli("--help")
    assert result.returncode == 0
    assert "calc" in result.stdout
    assert "convert" in result.stdout