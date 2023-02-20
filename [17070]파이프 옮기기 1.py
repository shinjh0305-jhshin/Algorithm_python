import sys
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]
dp = [[[-1] * 3 for _ in range(sz)] for _ in range(sz)]  # 0 : 가로, 1 : 세로, 2 : 대각선  # 기준 : 오른쪽 끝
dx, dy = [0, 1, 1], [1, 0, 1]


def dfs(cx=0, cy=1, d=0):
    if cx == sz - 1 and cy == sz - 1:
        dp[cx][cy][d] = 1
        return 1

    tmp = 0
    for i in range(3):
        if (i == 0 and d == 1) or (i == 1 and d == 0):
            continue
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < sz and 0 <= ny < sz and k[nx][ny] == 0:
            if i == 2 and (k[cx + 1][cy] == 1 or k[cx][cy + 1] == 1):  # 대각선 방향에서 나머지 두 칸이 벽인 경우
                continue
            if dp[nx][ny][i] != -1:
                tmp += dp[nx][ny][i]
            else:
                tmp += dfs(nx, ny, i)

    dp[cx][cy][d] = tmp
    return tmp


def operate():
    print(dfs())


operate()
