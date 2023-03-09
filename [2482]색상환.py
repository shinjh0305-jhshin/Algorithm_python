sz = int(input())
choice = int(input())
mod = 1000000003
dp = [[0] * 1003 for _ in range(1003)]


def operate():
    for i in range(1, sz + 1):
        dp[i][0] = 1
        dp[i][1] = i
        for j in range(2, choice + 1):
            dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % mod
    ans = (dp[sz - 3][choice - 1] + dp[sz - 1][choice]) % mod
    print(ans)


operate()