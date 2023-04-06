import sys
Input = sys.stdin.readline
target, nodes = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(nodes)]  # 비용, 고객
dp = []
INF, max_clients = 2134567890, 0


def initialize():
    global dp, max_clients
    max_clients = max(list(map(lambda x: x[1], k)))
    dp = [[INF] * (target + max_clients + 1) for _ in range(nodes + 1)]


def operate():
    dp[0][0] = 0
    for i in range(1, nodes + 1):
        cc, cp = k[i - 1]
        for j in range(cp):
            dp[i][j] = dp[i - 1][j]
        for j in range(cp, target + max_clients + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - cp] + cc)
    ans = INF
    for i in range(1, nodes + 1):
        ans = min(ans, min(dp[i][target:]))
    print(ans)


initialize()
operate()
