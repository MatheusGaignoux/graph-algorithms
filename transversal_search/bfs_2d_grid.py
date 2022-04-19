# In this example one  is going to  explore a grid with obtacles
# until reaches a point where the algorithm is supposed to stop.
import numpy as np

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def explore_neighbours(r, c, R, C, visited, m, rqueue, cqueue):
    for i in range(0, 4):
        rr = r + dr[i]
        cc = c + dc[i]

        # Bound location conditions
        cond1 = rr < 0 or cc < 0
        cond2 = rr >= R or cc >= C

        if all([cond1, cond2]): continue

        # Visited or blocked cells condition
        cond3 = visited[rr][cc] == True
        cond4 = m[rr][cc] == "#"

        if all([cond3, cond4]): continue

        rqueue.append(rr)
        cqueue.append(cc)
        visited[rr][cc] = True



