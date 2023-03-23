import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
k = [[] for _ in range(nodes + 1)]
s, e = 0, 0


def initialize():
    global s, e
    for _ in range(edges):
        x, y, c = map(int, Input().split())
        k[x].append([y, c])
        k[y].append([x, c])
    s, e = map(int, Input().split())


def dijkstra():
    pq = []
    visited = [-1] * (nodes + 1)

    visited[s] = sys.maxsize
    heappush(pq, [-sys.maxsize, s])

    while pq:
        cc, cn = heappop(pq)
        cc = -cc

        if cn == e:
            print(cc)
            return
        if visited[cn] < cc:
            continue
        for nn, tc in k[cn]:
            nc = min(cc, tc)
            if visited[nn] < nc:
                visited[nn] = nc
                heappush(pq, [-nc, nn])


initialize()
dijkstra()

