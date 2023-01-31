from sys import maxsize
target = int(input())
dp = [maxsize] * (target + 1)
dp[1] = 0
for i in range(1, target):
    if i + 1 <= target:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    if i * 2 <= target:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i * 3 <= target:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
print(dp[target])