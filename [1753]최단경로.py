import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
startNode = int(Input())
graph = [[] for _ in range(nodes + 1)]
for _ in range(edges):
    x, y, p = map(int, Input().split())
    graph[x].append((y, p))  # (node, price)
# Dijkstra
heap = []
INF = 2134567890
visited = [False] * (nodes + 1)
result = [INF] * (nodes + 1)
heappush(heap, (0, startNode))  # (price, node)
result[startNode] = 0
while heap:
    tmp = heappop(heap)
    curPrice = tmp[0]
    curNode = tmp[1]

    if visited[curNode]:
        continue
    visited[curNode] = True
    for tmp in graph[curNode]:
        nextNode = tmp[0]
        nextPrice = tmp[1] + curPrice
        if nextPrice < result[nextNode]:
            result[nextNode] = nextPrice
            heappush(heap, (nextPrice, nextNode))

for x in result[1:]:
    if x != INF:
        print(x)
    else:
        print("INF")
