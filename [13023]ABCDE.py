import sys
Input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
nodes, edges = map(int, Input().split())
graph = [[] for _ in range(nodes)]
visited = [False] * nodes
result = False

for _ in range(edges):
    x, y = map(int, Input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(node, depth):
    global result
    if depth == 5:
        result = True
        return
    visited[node] = True
    for nextNode in graph[node]:
        if not result and not visited[nextNode]:
            dfs(nextNode, depth + 1)
    visited[node] = False


for i in range(nodes):
    if not result:
        dfs(i, 1)

print(int(result))