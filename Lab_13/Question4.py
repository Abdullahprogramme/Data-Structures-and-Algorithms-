from HelperFunctions import *
from Question2 import GetShortestPath
import csv

def GetShortestDistanceBetweenCities(source,destination):
    # Write your code here
    with open('connections.csv', 'r') as file:
        reader = csv.reader(file)
        heading = next(reader)[1:]
        
        graph = {}
        for row in reader:
            place, conn = row[0], row[1:]
            
            AddNodes(graph, [place])
            for i in range(len(conn)):
                if conn[i] != '0' and conn[i] != '-1':

                    print(place, heading[i], conn[i])
                    AddEdges(graph, [(place, heading[i], int(conn[i]))], True)
    

    shortest = GetShortestPath(graph, source, destination)
    return shortest
if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))
    