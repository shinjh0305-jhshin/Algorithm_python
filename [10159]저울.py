import sys
Input = sys.stdin.readline
nodes = int(Input())
edges = int(Input())
route = [[False] * (nodes + 1) for _ in range(nodes + 1)]


def initialize():
    for _ in range(edges):
        x, y = map(int, Input().split())
        route[x][y] = True


def operate():
    for k in range(1, nodes + 1):
        for i in range(1, nodes + 1):
            if not route[i][k]:
                continue
            for j in range(1, nodes + 1):
                if route[i][k] and route[k][j]:
                    route[i][j] = True
    ans = []
    for i in range(1, nodes + 1):
        avail = nodes
        for j in range(1, nodes + 1):
            if i == j or route[i][j] or route[j][i]:
                avail -= 1
        ans.append(avail)
    print(*ans, sep='\n')


initialize()
operate()