import sys
Input = sys.stdin.readline
sz, target = map(int, Input().split())
k = [int(Input()) for _ in range(sz)]
k = list(set(k))
INF = 2134567890
dp = [[INF] * (target + 1) for _ in range(2)]
dp[0][0] = dp[1][0] = 0


def operate():
    cur = 0
    prev = 1
    for i in k:
        for j in range(1, target + 1):
            dp[cur][j] = dp[prev][j]
            if j >= i:
                dp[cur][j] = min(dp[cur][j], dp[cur][j - i] + 1)
        cur, prev = prev, cur

    if dp[prev][target] == INF:
        print(-1)
    else:
        print(dp[prev][target])


operate()
