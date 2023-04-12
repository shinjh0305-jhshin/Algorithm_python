import sys
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
INF = 2134567890
visited = [[INF] * (nodes + 1) for _ in range(nodes + 1)]


def initialize():
    for _ in range(edges):
        x, y, c = map(int, Input().split())
        visited[x][y] = c


def floyd_warshall():
    for x in range(1, nodes + 1):
        for i in range(1, nodes + 1):
            if visited[i][x] == INF:
                continue
            for j in range(1, nodes + 1):
                visited[i][j] = min(visited[i][j], visited[i][x] + visited[x][j])
    ans = INF
    for i in range(1, nodes + 1):
        ans = min(visited[i][i], ans)
    return ans if ans != INF else -1


initialize()
print(floyd_warshall())