import pytest
import subprocess
def script_1(com: str, path: str, text: str) -> bool:
    result = subprocess.run(f"{com} {path}", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        if text in result.stdout:
            return True
        else:
            return False
def test_one():
    assert script_1("ls", "/home", "us1"), "Fail"

# @pytest.mark.check
def test_two():
    assert script_1("ls", "/home", "kes") == False, "Fail"