import sys
from collections import deque
Input = sys.stdin.readline
nodes, edges, length, start = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
for _ in range(edges):
    x, y = map(int, Input().split())
    graph[x].append(y)

def bfs():
    qu = deque()
    visited = [False] * (nodes + 1)

    qu.append(start)
    visited[start] = True

    for _1 in range(length):
        iter = len(qu)
        for _2 in range(iter):
            curnode = qu.popleft()
            for nextnode in graph[curnode]:
                if not visited[nextnode]:
                    qu.append(nextnode)
                    visited[nextnode] = True

    res = sorted(qu)
    if res:
        print(*res, sep='\n')
    else:
        print(-1)


bfs()