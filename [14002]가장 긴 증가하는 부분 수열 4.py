from bisect import bisect_left
sz = int(input())
k = list(map(int, input().split()))


def operate():
    pos = [1] * sz
    x = [k[0]]
    for i in range(1, sz):
        if k[i] > x[-1]:
            x.append(k[i])
            pos[i] = len(x)
        else:
            idx = bisect_left(x, k[i])
            x[idx] = k[i]
            pos[i] = idx + 1
    print(len(x))

    cur_len = len(x)
    ans = []
    for i in range(sz - 1, -1, -1):
        if pos[i] == cur_len:
            ans.append(k[i])
            cur_len -= 1
    ans.reverse()
    print(*ans)


operate()