from HelperFunctions import *
from Question2 import GetShortestPath
def GetShortestPathGrid(grid,source,destination):
    # Write your code here
    adjlist = {}
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) not in adjlist and grid[i][j] != -1:
                adjlist[(i, j)] = []

            if i - 1 > -1 and grid[i-1][j] != -1 and grid[i][j] != -1:
                adjlist[(i, j)].append(((i-1, j), 1))
            if i + 1 < len(grid) and grid[i+1][j] != -1 and grid[i][j] != -1:
                adjlist[(i, j)].append(((i+1, j), 1))
            if j - 1 > -1 and grid[i][j-1] != -1 and grid[i][j] != -1:
                adjlist[(i, j)].append(((i, j-1), 1))
            if j + 1 < len(row) and grid[i][j+1] != -1 and grid[i][j] != -1:
                adjlist[(i, j)].append(((i, j+1), 1))
    
    shortest = GetShortestPath(adjlist, source, destination)
    return shortest

if __name__ == "__main__":
    grid =[[1, 1, 1], [-1, 1, 1], [1, -1, 1]]
    source = (0, 0)
    destination = (2,2)
    print(GetShortestPathGrid(grid, source, destination))


        