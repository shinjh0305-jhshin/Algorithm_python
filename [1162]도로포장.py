import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
nodes, edges, wraps = map(int, Input().split())
k = [[] for _ in range(nodes + 1)]
dp = [[sys.maxsize] * (wraps + 1) for _ in range(nodes + 1)]  # dp[node][wrapped]


def initialize():
    for _ in range(edges):
        x, y, c = map(int, Input().split())
        k[x].append([y, c])
        k[y].append([x, c])
    dp[1][0] = 0


def operate():
    pq = []
    heappush(pq, [0, 1, 0])  # acc_cost, node, wrapped

    while pq:
        cc, cn, cw = heappop(pq)
        if cn == nodes:
            print(cc)
            return
        if dp[cn][cw] < cc:
            continue
        for nn, tc in k[cn]:
            # 포장한다
            if cw < wraps:
                nc, nw = cc, cw + 1
                if dp[nn][nw] > nc:
                    dp[nn][nw] = nc
                    heappush(pq, [nc, nn, nw])
            # 포장 안한다
            nc, nw = cc + tc, cw
            if dp[nn][nw] > nc:
                dp[nn][nw] = nc
                heappush(pq, [nc, nn, nw])


initialize()
operate()
