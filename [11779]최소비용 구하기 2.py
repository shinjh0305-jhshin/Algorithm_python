import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
nodes = int(Input())
edges = int(Input())
k = [[] for _ in range(nodes + 1)]
s, e = 0, 0


def dijkstra():
    visited = [sys.maxsize] * (nodes + 1)
    prev_node = [-1] * (nodes + 1)
    pq = []
    heappush(pq, (0, s))
    visited[s] = 0

    while True:
        cc, cn = heappop(pq)
        if cn == e:
            break
        if visited[cn] < cc:
            continue
        for nn, tc in k[cn]:
            nc = cc + tc
            if visited[nn] > nc:
                visited[nn] = nc
                heappush(pq, (nc, nn))
                prev_node[nn] = cn

    route = []
    cn = e

    while cn != -1:
        route.append(cn)
        cn = prev_node[cn]
    route.reverse()

    print(visited[e], len(route), sep='\n')
    print(*route)


def operate():
    for _ in range(edges):
        x, y, c = map(int, Input().split())
        k[x].append([y, c])

    global s, e
    s, e = map(int, Input().split())

    dijkstra()


operate()