import sys
Input = sys.stdin.readline
sz = int(Input())
k = [[0, 0] for _ in range(sz + 1)]
for i in range(1, sz + 1):
    k[i] = list(map(int, Input().split()))
dp = [[0] * (sz + 1) for _ in range(sz + 1)]


def operate():
    for d in range(1, sz):  # 곱하는 행렬의 개수
        for l in range(1, sz - d + 1):  # 가장 왼쪽 행렬
            r = l + d  # 가장 오른쪽 행렬
            if d == 1:
                dp[l][r] = k[l][0] * k[l][1] * k[r][1]
            else:
                res = sys.maxsize
                for b in range(l, r):  # l부터 b까지 * b부터 r까지
                    left_muls = dp[l][b]
                    right_muls = dp[b + 1][r]
                    block_muls = k[l][0] * k[b][1] * k[r][1]
                    res = min(res, left_muls + right_muls + block_muls)
                dp[l][r] = res
    print(dp[1][sz])


operate()
