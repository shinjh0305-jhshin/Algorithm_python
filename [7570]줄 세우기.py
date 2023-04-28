sz = int(input())
k = list(map(int, input().split()))
dp = [0] * (sz + 1)


def operate():
    ans = 0

    for i in range(sz):
        idx = k[i]
        dp[idx] = dp[idx - 1] + 1
        ans = max(ans, dp[idx])

    print(sz - ans)


operate()
