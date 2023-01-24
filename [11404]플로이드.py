
import sys
Input = sys.stdin.readline


def initialize():
    for _ in range(edges):
        x, y, z = map(int, Input().split())
        result[x][y] = min(result[x][y], z)

    for x in range(1, nodes + 1):
        result[x][x] = 0


def operate():
    for k in range(1, nodes + 1):
        for i in range(1, nodes + 1):
            if result[i][k] == INF:
                continue
            for j in range(1, nodes + 1):
                tmp = result[i][k] + result[k][j]
                if tmp < result[i][j]:
                    result[i][j] = tmp

    for x in result[1:]:
        for y in x[1:]:
            print(0 if y == INF else y, end=' ')
        print()


nodes = int(Input())
edges = int(Input())
INF = 2134567890
result = [[INF] * (nodes + 1) for _ in range(nodes + 1)]

initialize()
operate()
