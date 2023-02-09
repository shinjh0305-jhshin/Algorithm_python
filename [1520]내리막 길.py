import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
dp = [[-1] * cols for _ in range(rows)]
dp[rows - 1][cols - 1] = 1
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(cx, cy):
    ret = 0
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] < k[cx][cy]:
            if dp[nx][ny] != -1:
                ret += dp[nx][ny]
            else:
                ret += dfs(nx, ny)
    dp[cx][cy] = ret
    return ret


print(dfs(0, 0))