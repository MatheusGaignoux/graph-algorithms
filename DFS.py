# DFS is a traversal algorithm that allow us to explore the nodes and edges of a graph. 
# Time complexity: O(V + E), i.e., it is directly proportional to size of the graph.

import time
import sys

def dfs(at, graph, visited):
    if visited[at]: return

    visited[at] = True

    neighbours = graph[at]
    for next in neighbours:
        path.append(next)
        print(path)
        time.sleep(.5)

        dfs(next, graph, visited)
        
        path.pop()
        print(path)
        time.sleep(.5)

if __name__ == "__main__":
    first = int(sys.argv[1])
    graph = []
    path = [first]
    visited = []

    for neighbours in sys.argv[2:]:
        graph.append(list(map(lambda x: int(x), neighbours.split(","))))
        visited.append(False)
    
    print(path)
    time.sleep(0.5)
    dfs(first, graph, visited)
