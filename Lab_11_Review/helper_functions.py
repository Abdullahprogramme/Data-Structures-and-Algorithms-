import csv

##############################################################################################
############################# COPY YOUR LAB10 FUNCTIONS HERE #################################
def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G

def addEdges(G, edges, directed=False):
    if directed == False:
        for i in edges:
            tup1 = (i[1], i[2])
            tup2 = (i[0], i[2])
            G[i[0]].append(tup1)
            G[i[1]].append(tup2)
    else:
        for i in edges:
            tup = (i[1], i[2])
            G[i[0]].append(tup)
    return G

def displayGraph(G):
    print(G)

def listOfNodes(G):
    nodes = []
    for key in G.keys():
        nodes.append(key)
    return nodes

def listOfEdges(G, directed=False):
    edges = []
    for nodes in G:
        for tup in G[nodes]:
            if directed == False:
                t1 = (nodes, tup[0], tup[1])
                t2 = (tup[0], nodes, tup[1])
                if t1 not in edges and t2 not in edges:
                    edges.append(t1)
            else:
                t = (nodes, tup[0], tup[1])
                edges.append(t)
    return edges


def getNeighbors(G, nodes):
    neighbors = []
    for tup in G[nodes]:
        if tup[0] not in neighbors:
            neighbors.append(tup[0])
    return neighbors

def removeNode(G, node):
    del G[node]
    for nodes in G:
        lst = []
        for tup in G[nodes]:
            if tup[0] != node:
                t = (tup[0], tup[1])
                lst.append(t)
        G[nodes] = lst

def removeNodes(G, nodes):
    for node in nodes:
        del G[node]

    for node in G:
        lst = []
        for tup in G[node]:
            if tup[0] not in nodes:
                t = (tup[0], tup[1])
                lst.append(t)
        G[node] = lst

def getNearestNeighbor(G, node):
    nearest = None
    val = float('inf')
    for tup in G[node]:
        if tup[1] < val:
            val = tup[1]
            nearest = tup[0]
    return nearest


##############################################################################################
############################# COMPLETE YOUR LAB11 FUNCTIONS HERE #############################

def in_out_degree(G):
    in_out = {}
    for node in G:
        out_degree = len(G[node])
        in_degree = sum(1 for x in G if node in getNeighbors(G, x)) 
        in_out[node] = (in_degree, out_degree)
    return in_out


def degree(G):
    degree = {}
    for node in G:
        degree[node] = len(G[node])
    return degree

def getInNeighbors(G, node):
    in_neighbors = []
    for key in G:
        for tup in G[key]:
            if tup[0] == node:
                in_neighbors.append(key)
    return in_neighbors

def getOutNeighbors(G, node):
    out_neighbors = []
    for tup in G[node]:
        out_neighbors.append(tup[0])
    return out_neighbors

def isNeighbor(G, node1, node2):
    if node2 in getNeighbors(G, node1):
        return True
    else:
        return False

##############################################################################

def initialize_matrix(rows, cols):
    return [[0 for i in range(cols)] for j in range(rows)]

def adjlst_to_adj_matrix(G):
    nodes = listOfNodes(G)
    matrix = initialize_matrix(len(nodes), len(nodes))
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if isNeighbor(G, nodes[i], nodes[j]):
                matrix[i][j] = 1
            else:
                matrix[i][j] = -1
    return matrix

##############################################################################

def csv_to_adj_list(filename):
    G = {}
    k = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if k == 0:
                nodes = row[1:]
            else:
                var = row
                place, conn = var[0], var[1:]
                G[place] = []
                for i in range(len(conn)):
                    if conn[i] != '0' and conn[i] != '-1':
                        tup = (nodes[i], int(conn[i]))
                        G[place].append(tup)
            k += 1
    return G