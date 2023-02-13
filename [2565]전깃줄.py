import sys
from bisect import bisect_left
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]


def operate():
    k.sort()
    lis = [k[0][1]]
    for i in range(1, sz):
        if lis[-1] < k[i][1]:
            lis.append(k[i][1])
        else:
            lis[bisect_left(lis, k[i][1])] = k[i][1]
    print(sz - len(lis))


operate()


