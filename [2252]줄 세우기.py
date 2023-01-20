import sys
from collections import deque
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
incomingNodes = [0 for _ in range(nodes + 1)]
for _ in range(edges):
    start, end = map(int, Input().split())
    graph[start].append(end)
    incomingNodes[end] += 1
qu = deque()
for i in range(1, nodes + 1):
    if incomingNodes[i] == 0:
        qu.append(i)
while qu:
    length = len(qu)
    for _ in range(length):
        node = qu.popleft()
        print(node, end=' ')
        for mov in graph[node]:
            incomingNodes[mov] -= 1
            if incomingNodes[mov] == 0:
                qu.append(mov)
