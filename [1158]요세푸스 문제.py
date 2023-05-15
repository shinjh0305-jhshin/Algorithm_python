sz, hop = map(int, input().split())
k = [str(i) for i in range(1, sz + 1)]


def operate():
    idx = 0
    ans = []

    for _ in range(sz):
        idx += hop - 1
        idx %= len(k)
        ans.append(k[idx])
        k.pop(idx)

    print("<" + ', '.join(ans) + ">")


operate()