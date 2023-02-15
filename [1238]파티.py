import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
nodes, edges, target = map(int, Input().split())
from_party = [[] for _ in range(nodes + 1)]
to_party = [[] for _ in range(nodes + 1)]
from_party_cost = [sys.maxsize] * (nodes + 1)
to_party_cost = [sys.maxsize] * (nodes + 1)


def move(graph, cost):
    pq = []
    heappush(pq, (0, target))
    cost[target] = 0

    while pq:
        cc, cn = heappop(pq)
        if cost[cn] < cc:
            continue

        for nn, tc in graph[cn]:
            nc = cc + tc
            if cost[nn] > nc:
                cost[nn] = nc
                heappush(pq, (nc, nn))


def initialize():
    for _ in range(edges):
        x, y, c = map(int, Input().split())
        from_party[x].append((y, c))
        to_party[y].append((x, c))


def operate():
    move(from_party, from_party_cost)
    move(to_party, to_party_cost)
    ans = 0
    for i in range(1, nodes + 1):
        ans = max(ans, from_party_cost[i] + to_party_cost[i])
    print(ans)


initialize()
operate()
