sz = int(input())
mod = 1000000000
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(sz + 1)]


def initialize():
    for i in range(1, 10):
        dp[1][i][1 << i] = 1


def operate():
    for l in range(1, sz):
        for e in range(0, 10):
            for h in range(0, 1 << 10):
                if dp[l][e][h]:
                    if e > 0:
                        dp[l + 1][e - 1][h | 1 << (e - 1)] = (dp[l + 1][e - 1][h | 1 << (e - 1)] + dp[l][e][h]) % mod
                    if e < 9:
                        dp[l + 1][e + 1][h | 1 << (e + 1)] = (dp[l + 1][e + 1][h | 1 << (e + 1)] + dp[l][e][h]) % mod
    ans = 0
    for e in range(0, 10):
        ans = (ans + dp[sz][e][(1 << 10) - 1]) % mod
    print(ans)


initialize()
operate()

