import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
nodes, sz, edges = map(int, Input().split())
item = [0] + list(map(int, Input().split()))
k = [[] for _ in range(nodes + 1)]


def initialize():
    for _ in range(edges):
        a, b, l = map(int, Input().split())
        k[a].append([b, l])
        k[b].append([a, l])


def dijkstra(sn):
    visited = [sys.maxsize] * (nodes + 1)
    pq = []
    visited[sn] = 0
    heappush(pq, [0, sn])
    ans = 0

    while pq:
        cc, cn = heappop(pq)
        if visited[cn] < cc:
            continue
        ans += item[cn]
        for nn, tc in k[cn]:
            nc = cc + tc
            if visited[nn] > nc and nc <= sz:
                visited[nn] = nc
                heappush(pq, [nc, nn])
    return ans


def operate():
    ans = 0
    for i in range(1, nodes + 1):
        ans = max(ans, dijkstra(i))
    print(ans)


initialize()
operate()
