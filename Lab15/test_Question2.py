import pytest
from sys import stderr
from Question2 import *

res = """{'value': 'begin', 'left': {}, 'right': {'value': 'do', 'left': {}, 'right': {'value': 'else', 'left': {}, 'right': {'value': 'end', 'left': {}, 'right': {'value': 'if', 'left': {}, 'right': {'value': 'then', 'left': {}, 'right': {'value': 'while', 'left': {}, 'right': {}}}}}}}}"""

question2_testcases = [
(res)
]   

@pytest.mark.parametrize("result", question2_testcases)
def test_question2(capsys, result):
    Question2()
    captured, _ = capsys.readouterr()
    assert captured[:-1] == result