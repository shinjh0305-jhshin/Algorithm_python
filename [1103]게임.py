import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [list(Input().rstrip()) for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = [[False] * cols for _ in range(rows)]
dp = [[0] * cols for _ in range(rows)]
ans = 0


def dfs(cx=0, cy=0, depth=1):
    global ans
    visited[cx][cy] = True
    d = ord(k[cx][cy]) - ord('0')
    dead_end = True
    for i in range(4):
        nx, ny = cx + dx[i] * d, cy + dy[i] * d
        if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] != 'H':
            dead_end = False
            if visited[nx][ny]:
                ans = -1
                return
            if not dp[nx][ny]:
                dfs(nx, ny, depth + 1)
            if ans == -1:
                return
            dp[cx][cy] = max(dp[cx][cy], dp[nx][ny] + 1)
    if dead_end:
        dp[cx][cy] = 1
    ans = max(ans, dp[cx][cy])

    visited[cx][cy] = False


dfs()
print(ans)
