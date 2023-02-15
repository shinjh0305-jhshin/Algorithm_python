import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
graph = [[] for _ in range(nodes + 1)]
x1, x2 = 0, 0
INF = sys.maxsize
start_to_A = [INF] * (nodes + 1)
end_to_A = [INF] * (nodes + 1)
x1_to_x2 = [INF] * (nodes + 1)


def initialize():
    global x1, x2
    for _ in range(edges):
        a, b, c = map(int, Input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    x1, x2 = map(int, Input().split())


def dijkstra(start, cost):
    pq = []
    cost[start] = 0
    heappush(pq, (0, start))

    while pq:
        cc, cn = heappop(pq)
        if cost[cn] < cc:
            continue
        for nn, tc in graph[cn]:
            nc = cc + tc
            if cost[nn] > nc:
                cost[nn] = nc
                heappush(pq, (nc, nn))


def operate():
    dijkstra(1, start_to_A)
    dijkstra(nodes, end_to_A)
    dijkstra(x1, x1_to_x2)

    # 1 -> x1 -> x2 -> end
    ans1 = INF
    if not (start_to_A[x1] == INF or x1_to_x2[x2] == INF or end_to_A[x2] == INF):
        ans1 = start_to_A[x1] + x1_to_x2[x2] + end_to_A[x2]

    # 1 -> x2 -> x1 -> end
    ans2 = INF
    if not (start_to_A[x2] == INF or x1_to_x2[x2] == INF or end_to_A[x1] == INF):
        ans2 = start_to_A[x2] + x1_to_x2[x2] + end_to_A[x1]

    if ans1 == INF and ans2 == INF:
        print(-1)
    else:
        print(min(ans1, ans2))


initialize()
operate()
