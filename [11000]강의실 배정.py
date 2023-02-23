import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
sz = int(Input())
k = [tuple(map(int, Input().split())) for _ in range(sz)]


def operate():
    k.sort(key=lambda x: x[0])
    pq = []
    ans = 0
    for s, e in k:
        if not pq or pq[0] > s:
            ans += 1
        else:
            heappop(pq)
        heappush(pq, e)
    print(ans)


operate()
