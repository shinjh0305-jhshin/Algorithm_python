import sys
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
INF = 2134567890
graph = [[INF] * (nodes + 1) for _ in range(nodes + 1)]


def initialize():
    for _ in range(edges):
        x, y = map(int, Input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    for x in range(nodes + 1):
        graph[x][x] = 0


def operate():
    for k in range(1, nodes + 1):
        for i in range(1, nodes + 1):
            if graph[i][k] == INF:
                continue
            for j in range(1, nodes + 1):
                tmp = graph[i][k] + graph[k][j]
                graph[i][j] = min(graph[i][j], tmp)

    ans = INF
    for i in range(1, nodes + 1):
        tmp = sum(graph[i][1:])
        if tmp < ans:
            ans = tmp
            ppl = i
    print(ppl)


initialize()
operate()