import sys

sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline

nodes, edges = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
visited = [False] * (nodes + 1)

for _ in range(edges):
    x, y = map(int, Input().split())
    graph[x].append(y);
    graph[y].append(x);


def DFS(node):
    visited[node] = True
    for nextNode in graph[node]:
        if not visited[nextNode]:
            DFS(nextNode)


ans = 0
for i in range(1, nodes + 1):
    if not visited[i]:
        ans += 1
        DFS(i)
print(ans)