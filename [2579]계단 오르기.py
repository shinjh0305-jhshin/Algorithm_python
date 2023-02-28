import sys
Input = sys.stdin.readline
sz = int(Input())
k = [int(Input()) for _ in range(sz)]
dp = [[0] * sz for _ in range(2)]  # 0 : 1계단 딛고 올라옴, 1 : 2계단 딛고 올라옴


def operate():
    if sz == 1:
        return k[0]
    if sz == 2:
        return k[0] + k[1]

    dp[0][0] = dp[1][0] = k[0]
    dp[0][1] = k[0] + k[1]
    dp[1][1] = k[1]

    for i in range(2, sz):
        dp[0][i] = dp[1][i - 1] + k[i]
        dp[1][i] = max(dp[0][i - 2], dp[1][i - 2]) + k[i]

    return max(dp[0][sz - 1], dp[1][sz - 1])


print(operate())
