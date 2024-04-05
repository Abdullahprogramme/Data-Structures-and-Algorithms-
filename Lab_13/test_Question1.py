import pytest
from Question1 import *
test_cases =[
    ([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)], [('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)],'A'),
    ([('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)], [('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)],'B'),
    ([('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)], [('D', 4), ('E', 5), ('F', 6), ('G', 7)],'C'),
    ([('D', 4), ('E', 5), ('F', 6), ('G', 7)], [('E', 5), ('F', 6), ('G', 7)],'D'),
    ([('E', 5), ('F', 6), ('G', 7)], [('F', 6), ('G', 7)],'E'),
    ([('F', 6), ('G', 7)], [('G', 7)],'F'),
]

@pytest.mark.parametrize("i", range(len(test_cases)))
def test_DeQueue(i):
    queue = test_cases[i][0]
    expected = test_cases[i][1]
    assert DeQueue(queue) == test_cases[i][2]
    assert queue == expected