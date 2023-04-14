import sys
Input = sys.stdin.readline
nodes = int(Input())
INF = 2134567890
visited = [[INF] * (nodes + 1) for _ in range(nodes + 1)]


def initialize():
    while True:
        x, y = map(int, Input().split())
        if x == -1:
            return
        visited[x][y] = visited[y][x] = 1


def operate():
    for k in range(1, nodes + 1):
        visited[k][0] = visited[k][k] = 0
        for i in range(1, nodes + 1):
            if visited[i][k] == INF:
                continue
            for j in range(1, nodes + 1):
                visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])

    res = [max(visited[i]) for i in range(nodes + 1)]
    ans = min(res)
    candid = list(filter(lambda x: res[x] == ans, range(1, nodes + 1)))

    print(ans, res.count(ans))
    print(*candid)


initialize()
operate()