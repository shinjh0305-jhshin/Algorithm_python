import sys
Input = sys.stdin.readline
sz = int(Input())
P = list(map(int, Input().split()))
dp = [[0, 0] for _ in range(sz)]


def operate():
    dp[0] = [P[0], P[0]] if P[0] >= 0 else [P[0], 0]
    ans = P[0]
    for i in range(1, sz):
        dp[i][0] = max(dp[i - 1][0] + P[i], P[i])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + P[i])
        ans = max(ans, max(dp[i][0], dp[i][1]))
    print(ans)


operate()
