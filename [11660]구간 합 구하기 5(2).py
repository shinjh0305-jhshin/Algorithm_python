import sys
input = sys.stdin.readline
sz, iter = map(int, input().split())

dp = [[0] * (sz + 1) for _ in range(sz + 1)]

for i in range(1, sz + 1):
    temp = [0] + list(map(int, input().split()))
    for j in range(1, sz + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + temp[j]

for i in range(iter):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)
