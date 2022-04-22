# In this example one  is going to  explore a grid with obtacles
# until reaches a point where the algorithm is supposed to stop.
import argparse
import numpy as np
import time

def explore_neighbours(r, c, R, C, m, visited, rqueue, cqueue):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(0, 4):
        rr = r + dr[i]
        cc = c + dc[i]

        # Bound location conditions
        cond1 = rr < 0 or cc < 0
        cond2 = rr > R or cc > C

        if any([cond1, cond2]): continue

        # Visited or blocked cells condition
        cond3 = visited[rr][cc] == "T"
        cond4 = m[rr][cc] == "#"

        if any([cond3, cond4]): continue

        rqueue.append(rr)
        cqueue.append(cc)
        visited[rr][cc] = True

def bfs_2d_grid(s, m):
    rqueue = []
    cqueue = []
    visited = np.full_like(m, False)
    R, C = tuple(np.array(m.shape) - 1)

    rqueue.append(s[0])
    cqueue.append(s[1])
    visited[s[0]][s[1]] = True

    while len(rqueue) > 0:
        r = rqueue.pop(0)
        c = cqueue.pop(0)

        if m[r][c] == "E": break

        explore_neighbours(r, c, R, C, m, visited, rqueue, cqueue)
        print(visited)
        time.sleep(1)

    return r, c

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--Starting")
    parser.add_argument("-d", "--Dimension")
    parser.add_argument("-o", "--Obstacles")
    parser.add_argument("-e", "--Exit")

    args = parser.parse_args()

    s = tuple(map(int, args.Starting.split(",")))
    dimension = tuple(map(int, args.Dimension.split(",")))
    obstacles = [(int(i[0]), int(i[1])) for i in map(lambda x: x.split(","), args.Obstacles.split(" "))]
    grid_exit = tuple(int(i) for i in args.Exit.split(","))

    m = np.full(dimension, ".")
    for obstacle in obstacles:
        m[obstacle[0]][obstacle[1]] = "#"
        
    m[grid_exit[0]][grid_exit[1]] = "E"

    print(m)
    r, c = bfs_2d_grid(s, m)
    print(r, c)
