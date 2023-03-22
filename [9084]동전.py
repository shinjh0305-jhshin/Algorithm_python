import sys
Input = sys.stdin.readline
tc = int(Input())
ans = []


def operate():
    coins = int(Input())
    coin = [0] + list(map(int, Input().split()))
    target = int(Input())
    dp = [[0] * (target + 1) for _ in range(coins + 1)]

    for i in range(1, coins + 1):
        c = coin[i]
        dp[i][0] = 1
        for j in range(1, target + 1):
            if j < c:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - c]

    ans.append(dp[coins][target])


for _ in range(tc):
    operate()
print(*ans, sep='\n')
