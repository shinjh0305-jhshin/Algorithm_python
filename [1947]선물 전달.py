dp = [0] * 1000005
dp[1] = 0
dp[2] = 1
target = int(input())
for i in range(3, target + 1):
    dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % 1000000000
print(dp[target])

