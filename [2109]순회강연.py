from heapq import heappop, heappush
import sys
Input = sys.stdin.readline
sz = int(Input())
if sz == 0:
    print(0)
    sys.exit()
k = [tuple(map(int, Input().split())) for _ in range(sz)]


def operate():
    k.sort(key=lambda x: x[1], reverse=True)
    pq = []
    idx = 0
    ans = 0

    for x in range(k[0][1], 0, -1):
        while idx < sz and k[idx][1] >= x:
            heappush(pq, -k[idx][0])
            idx += 1
        if pq:
            ans -= heappop(pq)
    print(ans)


operate()
