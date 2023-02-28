sz = int(input())
target = int(input())
k = list(map(int, input().split()))


def operate():
    k.sort()
    d = []
    for i in range(0, sz - 1):
        d.append(k[i + 1] - k[i])
    d.sort()
    print(sum(d[:sz - target]))


operate()