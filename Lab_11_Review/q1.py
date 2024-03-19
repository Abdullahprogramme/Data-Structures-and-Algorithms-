from helper_functions import *

'''
EXPECTED OUTPUT:

GRAPH
{1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}

IN NEIGHBORS
1 : [3]
2 : [1, 3]
3 : [4]
4 : [2, 4]

OUT NEIGHBORS
1 : [2]
2 : [4]
3 : [1, 2]
4 : [3, 4]

ADJACENCY MATRIX
[[-1, 1, -1, -1], [-1, -1, -1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]]

Sum of the in-degrees of all nodes, the sum of the out-degrees of all nodes and the total number of edges are all equal: True  
'''

vertices = [1, 2, 3, 4]
edges = [(1, 2), (2, 4), (3, 1), (3, 2), (4, 3), (4, 4)]
DG = addNodes({}, vertices)
DG = addEdges(DG, edges, True)
print(DG)


# Degree part
in_out = in_out_degree(DG)
print("\nIN DEGREES")
for i in in_out:
    print(i, ":", in_out[i][0])

print("\nOUT DEGREES")    
for i in in_out:
    print(i, ":", in_out[i][1])


# Neighbors part
print("\nIN NEIGHBORS")
for i in vertices:
    n = getInNeighbors(DG, i)
    print(i, ":", n)

print("\nOUT NEIGHBORS")
for i in vertices:
    n = getOutNeighbors(DG, i)
    print(i, ":", n)

# Adjacency matrix part
matrix = adjlst_to_adj_matrix(DG)
print("\nADJACENCY MATRIX")
for i in matrix:
    print(i)

# Sum of in-degrees, out-degrees and edges
in_out = in_out_degree(DG)
in_degrees = 0
out_degrees = 0
for i in in_out:
    in_degrees += in_out[i][0]
    out_degrees += in_out[i][1]
edges = 0
for i in in_out:
    edges += in_out[i][1]
print("\nSum of the in-degrees of all nodes, the sum of the out-degrees of all nodes and the total number of edges are all equal:", in_degrees == out_degrees == edges)