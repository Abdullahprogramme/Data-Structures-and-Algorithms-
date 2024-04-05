from HelperFunctions import *
from Question1 import *
def GetShortestPath(graph, source, destination):
    # Write your code here
    result = []
    PQ = []
    distance = {}
    prev = {}
    for node in graph:
        prev[node] = None
        if node == source:
            distance[node] = 0
            EnQueue(PQ, node, 0)
        else:
            distance[node] = float('inf')
            EnQueue(PQ, node, float('inf'))
    
    while not IsEmpty(PQ):
        v = DeQueue(PQ)

        for neigbours, weight in graph[v]:
            if distance[v] + weight < distance[neigbours]:
                distance[neigbours] = distance[v] + weight
                prev[neigbours] = v
                EnQueue(PQ, neigbours, distance[neigbours])
    
    city = destination
    if prev[destination] == None: return -1

    while city != source:
        result.insert(0, (prev[city], city, distance[city] - distance[prev[city]]))
        city = prev[city]

    return result

if __name__ == "__main__":
    graph = {'A': [('D', 2), ('E', 6), ('B', 7)], 'B': [('C', 3), ('A', 7)], 'C': [('B', 3), ('D', 2), ('G', 2)], 'D': [('A', 2), ('C', 2), ('F', 8)], 'E': [('A', 6), ('F', 9)], 'F': [('D', 8), ('E', 9), ('G', 4)], 'G': [('C', 2), ('F', 4)]}
    print(GetShortestPath(graph, 'A', 'G'))
    
    



