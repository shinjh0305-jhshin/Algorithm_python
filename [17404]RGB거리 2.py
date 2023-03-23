import sys
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]
INF = 2134567890
dp = [[0] * 3 for _ in range(sz)]


def operate():
    ans = INF
    for x in range(3):
        dp[0][x] = k[0][x]
        dp[0][(x - 1) % 3] = dp[0][(x + 1) % 3] = INF

        for i in range(1, sz):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][(j - 1) % 3], dp[i - 1][(j + 1) % 3]) + k[i][j]
        dp[sz - 1][x] = INF

        ans = min(ans, *dp[sz - 1])

    print(ans)


operate()