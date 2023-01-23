import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
nodes, edges, K = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
for _ in range(edges):
    x, y, c = map(int, Input().split())
    graph[x].append((y, c))  # (node, cost)
result = [sys.maxsize] * (nodes + 1)  # K번째 최소경로
visited = [0] * (nodes + 1)  # 방문 횟수
# dijkstra
heap = [(0, 1)]  # (cost, node)
while heap:
    x = heappop(heap)
    curCost = x[0]
    curNode = x[1]
    visited[curNode] += 1
    if visited[curNode] == K:
        result[curNode] = curCost
    elif visited[curNode] > K:
        continue
    for y in graph[curNode]:
        nextNode = y[0]
        nextCost = curCost + y[1]
        if visited[nextNode] >= K:
            continue
        heappush(heap, (nextCost, nextNode))
for x in result[1:]:
    if x == sys.maxsize:
        print(-1)
    else:
        print(x)