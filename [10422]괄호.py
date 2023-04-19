import sys
Input = sys.stdin.readline
tc = int(Input())
dp = [0] * 5001


def initialize():
    dp[0] = dp[2] = 1

    for i in range(4, 5001, 2):
        for j in range(2, i + 1):
            dp[i] += dp[j - 2] * dp[i - j]
        dp[i] %= 1000000007


def operate():
    x = [int(Input()) for _ in range(tc)]
    for i in x:
        print(dp[i])


initialize()
operate()
