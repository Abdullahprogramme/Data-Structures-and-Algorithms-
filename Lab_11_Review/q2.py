from helper_functions import *

'''
EXPECTED OUTPUT:

GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}

MAXIMUM IN-BOUND: Atlanta
MAXIMUM OUT-BOUND: Dallas
'''

# Create a graph
vertices = ['Dallas', 'Austin', 'Washington', 'Denver', 'Atlanta', 'Chicago', 'Houston']
edges = [('Dallas', 'Austin', 200), ('Dallas', 'Denver', 780), ('Dallas', 'Chicago', 900), ('Austin', 'Dallas', 200), ('Austin', 'Houston', 160), ('Washington', 'Dallas', 1300), ('Washington', 'Atlanta', 600), ('Denver', 'Atlanta', 1400), ('Denver', 'Chicago', 1000), ('Atlanta', 'Washington', 600), ('Atlanta', 'Houston', 800), ('Chicago', 'Denver', 1000), ('Houston', 'Atlanta', 800)]
G = addNodes({}, vertices)
G = addEdges(G, edges, True)
print(G)

def max_inbound(G):
    max_in = 0
    max_in_node = ''
    for node in G:
        in_degree = in_out_degree(G)[node][0]
        if in_degree > max_in:
            max_in = in_degree
            max_in_node = node
    return max_in_node

def max_outbound(G):
    max_out = 0
    max_out_node = ''
    for node in G:
        out_degree = in_out_degree(G)[node][1]
        if out_degree > max_out:
            max_out = out_degree
            max_out_node = node
    return max_out_node

print(f"MAXIMUM IN-BOUND: {max_inbound(G)}")
print(f"MAXIMUM OUT-BOUND: {max_outbound(G)}")