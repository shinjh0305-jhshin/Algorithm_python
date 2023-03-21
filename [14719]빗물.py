import sys

h, w = map(int, input().split())
k = list(map(int, input().split()))


def operate():
    ans = [sys.maxsize] * w
    ans[0] = ans[w - 1] = 0
    # 왼쪽에서 다가온다
    cur = k[0]
    for i in range(1, w - 1):
        if k[i] < cur:
            ans[i] = min(ans[i], cur - k[i])
        else:
            ans[i] = 0
            cur = k[i]
    # 오른쪽에서 다가온다
    cur = k[w - 1]
    for i in range(w - 2, 0, -1):
        if k[i] < cur:
            ans[i] = min(ans[i], cur - k[i])
        else:
            ans[i] = 0
            cur = k[i]
    print(sum(ans))


operate()
