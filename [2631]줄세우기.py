from bisect import bisect_left
sz = int(input())
k = [int(input()) for _ in range(sz)]
lis = [k[0]]


def operate():
    for i in range(1, sz):
        if k[i] > lis[-1]:
            lis.append(k[i])
        else:
            idx = bisect_left(lis, k[i])
            lis[idx] = k[i]
    print(sz - len(lis))


operate()