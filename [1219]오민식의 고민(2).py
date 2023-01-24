import sys
from collections import deque
Input = sys.stdin.readline


def bellmanford():
    for _ in range(nodes):
        for s in range(nodes):
            for e, c in graph[s]:
                if result[s] == INF:
                    continue
                elif result[s] + earning[e] - c > result[e]:
                    if _ == nodes - 1 and not visited[s]:
                        visited[s] = True
                        circularNode.append(s)
                    else:
                        result[e] = result[s] + earning[e] - c


def check_circular():
    while circularNode:
        cn = circularNode.popleft()
        for nn, cost in graph[cn]:
            if nn == end:
                return True
            if not visited[nn]:
                visited[nn] = True
                circularNode.append(nn)
    return False


nodes, start, end, edges = map(int, Input().split())
graph = [[] for _ in range(nodes)]
for _ in range(edges):
    s, e, c = map(int, Input().split())
    graph[s].append((e, c))
earning = list(map(int, Input().split()))
INF = -2134567890
root = [-1] * nodes
result = [INF] * nodes
result[start] = earning[start]
visited = [False] * nodes  # For circular traversing
circularNode = deque()

bellmanford()

if result[end] == INF:
    print("gg")
elif check_circular():
    print("Gee")
else:
    print(result[end])