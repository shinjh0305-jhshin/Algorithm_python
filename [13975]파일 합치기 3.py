import sys
from heapq import heappop, heappush, heapify
Input = sys.stdin.readline
tc = int(Input())


def operate():
    sz = int(Input())
    k = list(map(int, Input().split()))
    heapify(k)

    ans = 0
    while len(k) != 1:
        x1, x2 = heappop(k), heappop(k)
        ans += x1 + x2
        heappush(k, x1 + x2)
    print(ans)


for _ in range(tc):
    operate()
