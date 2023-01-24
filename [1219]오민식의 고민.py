import sys
Input = sys.stdin.readline


def bellmanford():
    for _ in range(nodes + 50):
        for s in range(nodes):
            for e, c in graph[s]:
                if result[s] == INF:
                    continue
                elif result[s] == -INF:
                    result[e] = -INF
                elif result[s] + earning[e] - c > result[e]:
                    if _ >= nodes - 1:
                        result[e] = -INF
                    else:
                        result[e] = result[s] + earning[e] - c


nodes, start, end, edges = map(int, Input().split())
graph = [[] for _ in range(nodes)]
for _ in range(edges):
    s, e, c = map(int, Input().split())
    graph[s].append((e, c))
earning = list(map(int, Input().split()))
INF = -2134567890
result = [INF] * nodes
result[start] = earning[start]

bellmanford()

if result[end] == INF:
    print("gg")
elif result[end] == -INF:
    print("Gee")
else:
    print(result[end])