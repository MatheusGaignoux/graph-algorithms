# DFS is a traversal algorithm that allow us to explore the nodes and edges of a graph. 
# Time complexity: O(V + E), i.e., it is directly proportional to the size of the graph.

import time
import sys

def dfs(path, graph, visited, components, count = None):
    at = path[-1]
    if visited[at]: return

    visited[at] = True
    components[at] = count
    neighbours = graph[at]
    
    for next in neighbours:
        path.append(next)
        print(path)
        time.sleep(.5)

        dfs(path, graph, visited, components, count)
        
        path.pop()
        print(path)
        time.sleep(.5)

# In order to run this script the starting node of the graph search as well as the graph needs to be passed as args.
# Each node must be represented as an integer.
# USAGE: python DFS.py (starting node: int) (node zero neighbors list) (node one neighbors list) ...
# EXEMPLE: python DFS.py 0 1,5 0,6 4 4 2,3,6 0,6 1,4,5
if __name__ == "__main__":
    first = int(sys.argv[1])
    graph = []

    for neighbours in sys.argv[2:]:
        graph.append(list(map(lambda x: int(x), neighbours.split(","))))
    
    n = len(graph)
    visited = [False] * n
    components = [None] * n
    path = [first]
    
    print(path)
    time.sleep(0.5)
    dfs(path, graph, visited, components)
