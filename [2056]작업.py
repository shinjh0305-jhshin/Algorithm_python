import sys
from collections import deque
Input = sys.stdin.readline
sz = int(Input())
in_edges = [0] * (sz + 1)
cost = [0] * (sz + 1)
time_elapsed = [0] * (sz + 1)
k = [[] for _ in range(sz + 1)]


def initialize():
    for i in range(1, sz + 1):
        tmp = list(map(int, Input().split()))
        cost[i] = tmp[0]
        in_edges[i] = tmp[1]
        for x in range(2, 2 + tmp[1]):
            k[tmp[x]].append(i)


def operate():
    qu = deque()
    for i in range(1, sz + 1):
        if in_edges[i] == 0:
            qu.append(i)
            time_elapsed[i] = cost[i]

    while qu:
        cn = qu.popleft()
        for nn in k[cn]:
            time_elapsed[nn] = max(time_elapsed[nn], time_elapsed[cn] + cost[nn])
            in_edges[nn] -= 1
            if in_edges[nn] == 0:
                qu.append(nn)

    print(max(time_elapsed))


initialize()
operate()

