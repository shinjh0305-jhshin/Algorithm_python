import sys
from collections import deque
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
k = [[] for _ in range(nodes + 1)]
in_edges = [0] * (nodes + 1)


def initialize():
    for _ in range(edges):
        x, y = map(int, Input().split())
        k[x].append(y)
        in_edges[y] += 1


def operate():
    qu = deque(list(filter(lambda x: in_edges[x] == 0, range(1, nodes + 1))))
    ans = [0] * (nodes + 1)

    turn = 1
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cn = qu.popleft()
            ans[cn] = turn
            for nn in k[cn]:
                in_edges[nn] -= 1
                if in_edges[nn] == 0:
                    qu.append(nn)
        turn += 1

    print(*ans[1:])


initialize()
operate()
