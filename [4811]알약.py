import sys
Input = sys.stdin.readline
dp = [[1] * 31 for _ in range(31)]


def initialize():
    for i in range(2, 31):
        for j in range(1, i + 1):
            if i != j:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]


def operate():
    ans = []
    while True:
        x = int(Input())
        if x == 0:
            break
        ans.append(dp[x][x])
    print(*ans, sep='\n')


initialize()
operate()
