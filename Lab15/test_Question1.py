import pytest
from sys import stderr
from Question1 import *

res = """{'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}
True
False
{'value': 4, 'left': {}, 'right': {}}
{'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}
{'value': 94, 'left': {}, 'right': {}}
{'value': 66, 'left': {}, 'right': {}}
[4, 50, 61, 66, 68, 76, 82, 88, 89, 94]
[68, 61, 50, 4, 66, 88, 76, 82, 89, 94]
[4, 50, 66, 61, 82, 76, 94, 89, 88, 68]
82"""

question1_testcases = [
(res)
]   

@pytest.mark.parametrize("result", question1_testcases)
def test_question1(capsys, result):
    Question1()
    captured, _ = capsys.readouterr()
    assert captured[:-1] == result