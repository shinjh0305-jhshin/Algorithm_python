import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline

nodes, edges, begin = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
for _ in range(edges):
    start, end = map(int, Input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(1, nodes + 1):
    graph[i].sort()


def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for nextNode in graph[node]:
        if not visited[nextNode]:
            visited[nextNode] = True
            dfs(nextNode)


def bfs():
    qu = deque()
    qu.append(begin)
    visited[begin] = True

    while qu:
        curNode = qu.popleft()
        print(curNode, end=' ')
        for nextNode in graph[curNode]:
            if not visited[nextNode]:
                visited[nextNode] = True
                qu.append(nextNode)


visited = [False] * (nodes + 1)
dfs(begin)
print()
visited = [False] * (nodes + 1)
bfs()