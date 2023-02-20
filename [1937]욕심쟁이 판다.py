import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
sz = int(Input())
graph = [list(map(int, Input().split())) for _ in range(sz)]
dp = [[sys.maxsize] * sz for _ in range(sz)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def dfs(cx, cy):
    res = 0
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < sz and 0 <= ny < sz and graph[nx][ny] > graph[cx][cy]:
            if dp[nx][ny] == sys.maxsize:
                dfs(nx, ny)
            res = max(res, dp[nx][ny])
    dp[cx][cy] = res + 1  # 내 칸도 더하기


def operate():
    ans = 0
    for i in range(sz):
        for j in range(sz):
            if dp[i][j] == sys.maxsize:
                dfs(i, j)
            ans = max(ans, dp[i][j])
    print(ans)


operate()
