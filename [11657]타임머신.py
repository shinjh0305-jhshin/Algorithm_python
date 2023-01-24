import sys
Input = sys.stdin.readline


def bellmanFord():
    for _ in range(nodes - 1):
        for start in range(1, nodes + 1):
            for end, cost in graph[start]:
                if result[start] != INF and result[start] + cost < result[end]:
                    result[end] = result[start] + cost


nodes, edges = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
for i in range(edges):
    s, e, c = map(int, Input().split())
    graph[s].append((e, c))
INF = 2134567890
result = [INF] * (nodes + 1)
result[1] = 0

bellmanFord()

# Negative edge cycle
flag = True
for s in range(1, nodes + 1):
    for e, c in graph[s]:
        if result[s] != INF and result[s] + c < result[e]:
            flag = False
            break
if not flag:
    print(-1)
else:
    for x in result[2:]:
        print(x if x != INF else -1)