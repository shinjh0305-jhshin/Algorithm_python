import sys
from itertools import combinations
N = int(input())
num = list(map(int, input().split()))


def choose():
    ans = [sys.maxsize, sys.maxsize]
    min_num = [0, 0, 0]  # 01, 23, 45 중에서 최댓값 모임
    min_num[0] = min(num[0], num[5])
    min_num[1] = min(num[1], num[4])
    min_num[2] = min(num[2], num[3])

    for tmp in combinations(min_num, 2):
        ans[0] = min(ans[0], sum(tmp))
    for tmp in combinations(min_num, 3):
        ans[1] = min(ans[1], sum(tmp))
    return ans


def operate():
    if N == 1:
        print(sum(num) - max(num))
        return
    min_1 = min(num)
    min_2, min_3 = choose()

    ans = 0
    # 3면
    ans += min_3 * 4
    # 2면
    ans += 4 * (N - 2) * min_2  # 윗면
    ans += 4 * (N - 1) * min_2  # 중간면 + 아랫면
    # 1면
    ans += (N - 2) * (N - 2) * min_1  # 윗면
    ans += 4 * (N - 1) * (N - 2) * min_1  # 중간면 + 아랫면

    print(ans)


operate()
