import csv

def addVertices(G: dict, vertices: list):
    for i in vertices: # iterate through the list of vertices
        if i not in G:
            G[i] = [] # add the vertex to the graph as a key with an empty list as the value

def addEdges(G: dict, edges: list):
    for i in edges:
        tup = (i[1], i[2])
        G[i[0]].append(tup) # add the edge to the graph as a tuple with the destination and weight

def create_flight_network(filename: str, option: int):
    with open(filename, 'r') as file:
        reader = csv.reader(file) # read the csv file
        headings = next(reader)
        graph = {}

        all_vertices = []
        all_edges = []
        for row in reader:
            if row[0] not in all_vertices: # if the origin city is not in the list of vertices, add it
                all_vertices.append(row[0])
            from_, to, duration, distance = row
            if option == 1: # if the option is 1, add the edge with the duration as the weight
                all_edges.append((from_, to, int(duration)))
            elif option == 2:   # if the option is 2, add the edge with the distance as the weight
                all_edges.append((from_, to, int(distance)))

        addVertices(graph, all_vertices)
        addEdges(graph, all_edges)
        
    return graph

def get_flight_connections(graph: dict, city: str, option: str) -> list:
    connections = []
    if city not in graph:
        return connections
    if option == 'o': # if the option is 'o', get the outgoing connections by iterating through the edges of the city
        for edge in graph[city]:
            connections.append(edge[0])
    elif option == 'i': # if the option is 'i', get the incoming connections by iterating through the keys of the graph
        for key in graph:
            for edge in graph[key]:
                if edge[0] == city:
                    connections.append(key)
    return connections

def get_number_of_flight_connections(graph: dict, 
                                     city: str, 
                                     option: str) -> int:
    connections = get_flight_connections(graph, city, option) # get the connections and return the length of the list
    return len(connections)

def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    if origin not in graph:
        return None
    for edge in graph[origin]: # iterate through the edges of the origin city
        if edge[0] == destination: # if matched return the weight
            return edge[1]
    return -1

def add_flight(graph: dict, origin: str, destination: str, weight: int):
    if origin not in graph:
        print(f"{origin} not accessed by graph")
        return
    if destination not in graph:
        print(f"{destination} not accessed by graph")
        return
    
    for i, edge in enumerate(graph[origin]): # iterate in the graph and check if the destination is already in the edges
        if destination == edge[0]:
            graph[origin][i] = (destination, weight)
            return
    
    addEdges(graph, [(origin, destination, weight)]) # if the destination is not in the edges, add the edge

def add_airport(graph: dict, city: str, destination: str, weight: int):
    if city in graph:
        print(f"{city} already exists")
        return
    addVertices(graph, [city]) # add the city to the graph
    addEdges(graph, [(city, destination, weight)]) # add the different connections of the city

def get_secondary_flights(graph: dict, city: str):
    if city not in graph:
        return None
    secondary_flights = []
    connections = get_flight_connections(graph, city, 'o') # get the outgoing connections of the city
    for connection in connections:
        for edge in graph[connection]:
            if edge[0] not in secondary_flights: # iterate through the edges of the connections and add those escondary connections
                secondary_flights.append(edge[0])
    return secondary_flights

def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    common = 0
    connectionsA = get_flight_connections(graph, cityA, 'o') # get the outgoing connections of the city A
    connectionsB = get_flight_connections(graph, cityB, 'o') # get the outgoing connections of the city B
    for connection in connectionsA:
        if connection in connectionsB: # iterate through the connections of city A and check if it is in the connections of city B
            common += 1 # increment the variable if it is in both
    return common

def remove_flight(graph: dict, origin: str, destination: str):
    if origin not in graph:
        print(f"{origin} not accessed by graph")
        return
    if destination not in graph:
        print(f"{destination} not accessed by graph")
        return
    
    for i, edge in enumerate(graph[origin]): # iterate through the edges of the origin city and remove the destination
        if edge[0] == destination:
            graph[origin] = graph[origin][:i] + graph[origin][i+1:]
    for i, edge in enumerate(graph[destination]): # iterate through the edges of the destination city and remove the origin
        if edge[0] == origin:
            graph[destination] = graph[destination][:i] + graph[destination][i+1:]

def remove_airport(graph: dict, city: str):
    if city not in graph:
        print(f"{city} not accessed by graph")
        return
    del graph[city] # delete the city from the graph
    for key in graph:
        for i, edge in enumerate(graph[key]):
            if edge[0] == city: # iterate through the edges of the graph and remove the city from the edges
                graph[key] = graph[key][:i] + graph[key][i+1:]

def DFS_all_routes(graph: dict,
                    origin: str, 
                    destination: str,
                    route: list, 
                    all_routes: list):
    if len(route) > 1 and origin == destination: # if the origin is the destination, add the route to the list
        all_routes.append(route.copy())
    else:
        # Visit each neighbor of the current city
        for neighbor, _ in graph[origin]:
            if neighbor not in route or (neighbor == destination and len(route) > 1): # if the neighbor is not in the route make a recursive call
                route.append(neighbor)
                DFS_all_routes(graph, neighbor, destination, route, all_routes)
                route.pop() # remove the neighbor from the route after the recursive call
    return all_routes

def find_all_routes(graph: dict, origin: str, destination: str):
    all_routes = []
    if origin not in graph or destination not in graph:
        return None
    if origin == destination:
        return []
    route = [origin]
    all_routes = DFS_all_routes(graph, origin, destination, route, all_routes) # call the DFS function and find the routes
    return all_routes


def DFS_layovers(graph: dict, origin: str, destination: str, 
                 route: list, 
                 layovers_lst: list):
    if len(route) > 1 and origin == destination: # if the origin is the destination, add the number of layovers to the list
        layovers_lst.append(len(route) - 2)
    else:
        # Visit each neighbor of the current city
        for neighbor, _ in graph[origin]:
            if neighbor not in route or (neighbor == destination and len(route) > 1): # if the neighbor is not in the route make a recursive call
                route.append(neighbor)
                DFS_layovers(graph, neighbor, destination, route, layovers_lst)
                route.pop() # remove the neighbor from the route after the recursive call
    return layovers_lst

def find_number_of_layovers(graph: dict, origin: str, destination: str):
    route = [origin]
    layovers_lst = []
    if origin not in graph or destination not in graph:
        return None
    if origin == destination:
        return []
    layovers_lst = DFS_layovers(graph, origin, destination, route, layovers_lst) # call the DFS function and find the number of layovers
    return sorted(layovers_lst) # return the sorted list of layovers