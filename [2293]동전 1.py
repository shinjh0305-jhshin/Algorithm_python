import sys
Input = sys.stdin.readline
sz, target = map(int, Input().split())
k = [int(Input()) for _ in range(sz)]
dp = [[0] * (target + 1) for _ in range(2)]


def operate():
    prev = 0
    cur = 1
    dp[0][0] = dp[1][0] = 1

    for i in k:
        for j in range(1, target + 1):
            dp[cur][j] = dp[prev][j]
            if j >= i:
                dp[cur][j] += dp[cur][j - i]
        prev, cur = cur, prev

    print(dp[prev][target])


operate()