import pytest
from Question2 import GetShortestPath
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
testcases = [-1, [('A', 'B', 7)], [('A', 'D', 2), ('D', 'C', 2)], [('A', 'D', 2)], [('A', 'E', 6)], [('A', 'D', 2), ('D', 'F', 8)], [('A', 'D', 2), ('D', 'C', 2), ('C', 'G', 2)]]
graph = {'A': [('D', 2), ('E', 6), ('B', 7)], 'B': [('C', 3), ('A', 7)], 'C': [('B', 3), ('D', 2), ('G', 2)], 'D': [('A', 2), ('C', 2), ('F', 8)], 'E': [('A', 6), ('F', 9)], 'F': [('D', 8), ('E', 9), ('G', 4)], 'G': [('C', 2), ('F', 4)]}

@pytest.mark.parametrize("i", range(len(nodes)))
def test_GetShortestPath(i):
    assert GetShortestPath(graph, 'A', nodes[i]) == testcases[i]
