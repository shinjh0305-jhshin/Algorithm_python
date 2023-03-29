sz = int(input())
dp = [0] * (sz + 1)


def operate():
    if sz <= 6:
        print(sz)
        return
    for i in range(7):
        dp[i] = i
    for i in range(6, sz + 1):
        dp[i] = dp[i - 1] + 1
        dp[i] = max(dp[i], dp[i - 3] * 2)
        dp[i] = max(dp[i], dp[i - 4] * 3)
        dp[i] = max(dp[i], dp[i - 5] * 4)
    print(dp[sz])


operate()
