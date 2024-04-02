from Graphs_all import *

G = create_flight_network('flight_network.csv', 1)
# for i in G:
#     print(i, G[i])

print(Dijkstra_shortest_route(G, 'Vancouver', 'Toronto'))  # Expected output: ['Vancouver', 'Calgary', 'Toronto']
print(Dijkstra_shortest_route(G, 'Dubai', 'Vancouver'))  # Expected output: ['Dubai', 'San Francisco', 'Vancouver']
print(Dijkstra_shortest_route(G, 'Boston', 'Chicago'))  # Expected output: ['Boston', 'Chicago']
print(Dijkstra_shortest_route(G, 'Los Angeles', 'Washington'))  # Expected output: ['Los Angeles', 'Washington']
print(Dijkstra_shortest_route(G, 'Houston', 'Dubai'))  # Expected output: ['Houston', 'Dubai']
print(Dijkstra_shortest_route(G, 'Dallas', 'Jamaica'))  # Expected output: ['Dallas', 'Jamaica']
print(Dijkstra_shortest_route(G, 'Orlando', 'Dubai'))  # Expected output: ['Orlando', 'Dubai']
print(Dijkstra_shortest_route(G, 'Miami', 'Dubai'))  # Expected output: ['Miami', 'Dubai']
print(Dijkstra_shortest_route(G, 'Mexico City', 'London'))  # Expected output: ['Mexico City', 'London']
print(Dijkstra_shortest_route(G, 'Barcelona', 'Dubai'))  # Expected output: ['Barcelona', 'Dubai']
print(Dijkstra_shortest_route(G, 'London', 'Dubai'))  # Expected output: ['London', 'Dubai']
print(Dijkstra_shortest_route(G, 'Toronto', 'Boston'))  # Expected output: ['Toronto', 'Boston']
print(Dijkstra_shortest_route(G, 'Montreal', 'Ottawa'))  # Expected output: ['Montreal', 'Ottawa']
print(Dijkstra_shortest_route(G, 'Ottawa', 'Montreal'))  # Expected output: ['Ottawa', 'Montreal']
print(Dijkstra_shortest_route(G, 'Calgary', 'Vancouver'))  # Expected output: ['Calgary', 'Vancouver']
print(Dijkstra_shortest_route(G, 'Rio de Janeiro', 'Dubai'))  # Expected output: ['Rio de Janeiro', 'Dubai']
print(Dijkstra_shortest_route(G, 'Sao Paulo', 'Dubai'))  # Expected output: ['Sao Paulo', 'Dubai']
print(Dijkstra_shortest_route(G, 'Lima', 'Sao Paulo'))  # Expected output: ['Lima', 'Sao Paulo']
print(Dijkstra_shortest_route(G, 'Buenos Aires', 'Rio de Janeiro'))  # Expected output: ['Buenos Aires', 'Rio de Janeiro']
print(Dijkstra_shortest_route(G, 'Caracas', 'Mexico City'))  # Expected output: ['Caracas', 'Mexico City']