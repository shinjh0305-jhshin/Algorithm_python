N, K = map(int, input().split())
mod = 1000000000
dp = [[1] * 202 for _ in range(202)]


def operate():
    for i in range(1, N + 1):
        for j in range(2, K + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod
    print(dp[N][K])


operate()
