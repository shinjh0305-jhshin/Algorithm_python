import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
tb = ["0" * (cols + 1)]
for _ in range(rows):
    tb.append("0" + Input().rstrip())
dp = [[0] * (cols + 1) for _ in range(rows + 1)]


def operate():
    ans = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if tb[i][j] == "1":
                dp[i][j] = min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) + 1
                ans = max(ans, dp[i][j])
    print(ans ** 2)


operate()
