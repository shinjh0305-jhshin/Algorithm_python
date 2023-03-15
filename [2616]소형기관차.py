sz = int(input())
k = [0] + list(map(int, input().split()))
l = int(input())
dp = [[0] * (sz + 1) for _ in range(4)]
acc_sum = [0] * (sz + 1)


def operate():
    for i in range(1, sz + 1):
        acc_sum[i] = acc_sum[i - 1] + k[i]
    for i in range(1, 4):
        for j in range(i * l, sz + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - l] + acc_sum[j] - acc_sum[j - l])
    print(dp[3][sz])


operate()