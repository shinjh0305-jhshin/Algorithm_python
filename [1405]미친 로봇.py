import sys
sys.setrecursionlimit(10 ** 6)
visited = [[False] * 29 for _ in range(29)]
cx, cy = 14, 14
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
tmp = list(map(int, input().split()))
sz, p = tmp[0], list(map(lambda x: int(x) / 100, tmp[1:]))
ans = 0


def dfs(depth=0, x=14, y=14, cur_p=float(1)):
    if depth == sz:
        global ans
        ans += cur_p
        return
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not visited[nx][ny]:
            dfs(depth + 1, nx, ny, cur_p * p[i])
    visited[x][y] = False


dfs()
print(ans)