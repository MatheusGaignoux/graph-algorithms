# DFS is a traversal algorithm that allow us to explore the nodes and edges of a graph. 
# Time complexity: O(V + E), i.e., it is directly proportional to size of the graph.

import time
import sys

def dfs(at, graph, visited, path = []):
    if visited[at]: 
        path.append(at)
        print(path)
        time.sleep(0.5) 
        path.pop()
        print(path)
        time.sleep(0.5)
        return
        
    visited[at] = True
    path.append(at)
    print(path)
    time.sleep(0.5)

    neighbours = graph[at]
    for next in neighbours:
        dfs(next, graph, visited, path)

if __name__ == "__main__":
    first = int(sys.argv[1])
    graph = []
    path = []
    visited = []

    i = 0
    for neighbours in sys.argv[2:]:
        graph.append(list(map(lambda x: int(x), neighbours.split(","))))
        visited.append(False)
    
    dfs(first, graph, visited, [])