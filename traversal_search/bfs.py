import sys

def solve(graph, s):
    # definitions
    n = len(graph)
    queue = []
    visited = [False] * n
    prev = [None] * n

    visited[s] = True
    queue.append(s)

    while len(queue) > 0:
        node = queue.pop(0)
        neighbours = graph[node]

        for next in neighbours:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                prev[next] = node
        
    return prev

def reconstruct_path(s, e, prev):
    # Reconstruct path going backwards from e
    path = []
    at = prev[e]
    while at is not None:
        path.append(at)
        at = prev[at]
    
    path.reverse()

    if path[0] == s:
        return path
    return []

def bfs(graph, s, e):
    prev = solve(graph, s)

    return reconstruct_path(s, e, prev)

if __name__ == "__main__":
    first = int(sys.argv[1])
    last = int(sys.argv[2])
    graph = []

    for neighbours in sys.argv[3:]:
        graph.append(list(map(lambda x: int(x), neighbours.split(","))))

    path = bfs(graph, first, last)
    print(path)
