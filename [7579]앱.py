sz, target = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0] * (sum(cost) + 1) for _ in range(2)]


def operate():
    prev, cur = 0, 1
    sum_cost = sum(cost)
    for i in range(1, sz + 1):
        for j in range(1, sum_cost + 1):
            if j < cost[i]:
                dp[cur][j] = dp[prev][j]
            else:
                dp[cur][j] = max(dp[prev][j], dp[prev][j - cost[i]] + mem[i])
        prev, cur = cur, prev
    for j in range(1, sum_cost + 1):
        if dp[prev][j] >= target:
            print(j)
            return


operate()
