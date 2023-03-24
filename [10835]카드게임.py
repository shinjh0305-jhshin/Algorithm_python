import sys
Input = sys.stdin.readline
sz = int(Input())
left = list(map(int, Input().split()))
right = list(map(int, Input().split()))
dp = [[0] * (sz + 1) for _ in range(sz + 1)]

for i in range(sz - 1, -1, -1):
    for j in range(sz - 1, -1, -1):
        if right[j] < left[i]:
            dp[i][j] = max(dp[i][j + 1] + right[j], dp[i + 1][j], dp[i + 1][j +1])
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[0][0])