from bisect import bisect_left
import sys
Input = sys.stdin.readline
sz = int(Input())
k = list(map(int, Input().split()))
lis = [-sys.maxsize]  # LIS 길이를 구하기 위한 이분 탐색 리스트
dp = [0] * sz  # LIS를 구하기 위한 dp 리스트


def get_lis():
    for i in range(sz):
        if k[i] > lis[-1]:
            lis.append(k[i])
            dp[i] = len(lis) - 1
        else:
            upper_bound = bisect_left(lis, k[i])
            lis[upper_bound] = k[i]
            dp[i] = upper_bound
    print(len(lis) - 1)

    seq = []
    cur = len(lis) - 1
    for i in range(sz - 1, -1, -1):
        if dp[i] == cur:
            seq.append(k[i])
            cur -= 1
    print(*reversed(seq))


get_lis()
