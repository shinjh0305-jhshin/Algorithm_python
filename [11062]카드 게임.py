import sys
Input = sys.stdin.readline
tc = int(Input())


def operate():
    sz = int(Input())
    k = list(map(int, Input().split()))
    dp = [[0] * sz for _ in range(sz)]

    acc_sum = [0]  # 누적합을 구한다
    for i in range(sz):
        acc_sum.append(acc_sum[-1] + k[i])
    for i in range(sz):
        dp[i][i] = k[i]

    for x in range(1, sz):  # 대각선 모양의 dp 순회
        i, j = 0, x
        while j < sz:  # max(오른쪽 가져가기, 왼쪽 가져가기)
            dp[i][j] = max(k[j] + (acc_sum[j] - acc_sum[i]) - dp[i][j - 1],
                           k[i] + (acc_sum[j + 1] - acc_sum[i + 1]) - dp[i + 1][j])
            i, j = i + 1, j + 1
    print(dp[0][sz - 1])


for _ in range(tc):
    operate()
