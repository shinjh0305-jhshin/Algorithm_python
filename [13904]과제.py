from heapq import heappush, heappop
import sys
Input = sys.stdin.readline
sz = int(Input())
k = [tuple(map(int, Input().split())) for _ in range(sz)]


def operate():
    k.sort(reverse=True)
    idx, ans = 0, 0
    qu = []
    for day in range(k[0][0], 0, -1):
        while idx < sz and k[idx][0] >= day:
            heappush(qu, -k[idx][1])
            idx += 1
        if qu:
            ans -= heappop(qu)
    print(ans)


operate()