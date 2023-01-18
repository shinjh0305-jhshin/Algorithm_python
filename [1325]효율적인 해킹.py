import sys
from collections import deque
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
for _ in range(edges):
    start, end = map(int, Input().split())
    graph[start].append(end)
connected = [0] * (nodes + 1)


def bfs(node):
    qu = deque()
    qu.append(node)
    visited[node] = True
    while qu:
        curnode = qu.popleft()
        for nextnode in graph[curnode]:
            if not visited[nextnode]:
                visited[nextnode] = True
                connected[nextnode] += 1
                qu.append(nextnode)


for node in range(1, nodes + 1):
    visited = [False] * (nodes + 1)
    bfs(node)
maxNum = max(connected)
print(*list(filter(lambda x: connected[x] == maxNum, range(1, nodes + 1))))