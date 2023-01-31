sz = int(input())
dp = [[1] * 10 for _ in range(2)]
dp[0][0] = 0
mod = 1000000000

def operate():
    p = 1
    c = 0
    for i in range(sz - 1):
        p, c = c, p
        for j in range(0, 10):
            if j == 0:
                dp[c][0] = dp[p][1]
            elif j == 9:
                dp[c][9] = dp[p][8]
            else:
                dp[c][j] = (dp[p][j - 1] + dp[p][j + 1]) % mod
    print(sum(dp[c]) % mod)


operate()