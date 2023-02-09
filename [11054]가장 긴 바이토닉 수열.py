from bisect import bisect_left
sz = int(input())
k = list(map(int, input().split()))
dp = [[0] * sz for _ in range(2)]


def left_traverse():
    lis_tmp = [k[0]]
    dp[0][0] = 1
    for i in range(1, len(k)):
        if k[i] > lis_tmp[-1]:
            lis_tmp.append(k[i])
            dp[0][i] = len(lis_tmp)
        else:
            idx = bisect_left(lis_tmp, k[i])
            lis_tmp[idx] = k[i]
            dp[0][i] = idx + 1


def right_traverse():
    lis_tmp = [k[-1]]
    dp[1][-1] = 1
    for i in range(len(k) - 2, -1, -1):
        if k[i] > lis_tmp[-1]:
            lis_tmp.append(k[i])
            dp[1][i] = len(lis_tmp)
        else:
            idx = bisect_left(lis_tmp, k[i])
            lis_tmp[idx] = k[i]
            dp[1][i] = idx + 1


def operate():
    left_traverse()
    right_traverse()

    ans = -1
    for i in range(sz):
        ans = max(ans, dp[0][i] + dp[1][i])
    print(ans - 1)


operate()