import sys
from DFS import dfs

def find_components_dfs(graph, visited, components):
    count = 0
    for i in range(0, len(visited)):
        path = [i]
        if not visited[i]:
            dfs(i, graph, visited, path, components, count)
            count = count + 1
    return (count, components)

if __name__ == "__main__":
    graph = []
    visited = []
    components = []

    for neighbours in sys.argv[1:]:
        graph.append(list(map(lambda x: int(x), neighbours.split(","))))
        visited.append(False)
        components.append(0)

    count, components = find_components_dfs(graph, visited, components)
    print("number of connected components:", count)
    print("labels:", components)
