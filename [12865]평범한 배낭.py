import sys
Input = sys.stdin.readline
sz, weight = map(int, Input().split())
dp = [[0] * (weight + 1) for _ in range(sz + 1)]
k = [(0, 0)] + [tuple(map(int, Input().split())) for _ in range(sz)]


def operate():
    for i in range(1, sz + 1):
        cw, cc = k[i]
        for j in range(1, weight + 1):
            if j < cw:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - cw] + cc, dp[i - 1][j])
    print(dp[sz][weight])


operate()
