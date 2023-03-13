sz, groups = map(int, input().split())
k = list(map(int, input().split()))
diff = []


def operate():
    for i in range(0, sz - 1):
        diff.append(k[i + 1] - k[i])
    diff.sort()
    ans = sum(diff[:(sz - groups)])
    print(ans)


operate()
