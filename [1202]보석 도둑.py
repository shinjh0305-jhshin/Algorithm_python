import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
jewels, bags = map(int, Input().split())
jewel = [tuple(map(int, Input().split())) for _ in range(jewels)]  # weight, price
bag = [int(Input()) for _ in range(bags)]  # limit


def operate():
    jewel.sort()
    bag.sort()
    pq = []
    jewel_idx = 0
    ans = 0
    for k in bag:
        while jewel_idx < jewels and jewel[jewel_idx][0] <= k:
            heappush(pq, -jewel[jewel_idx][1])
            jewel_idx += 1
        if pq:
            ans -= heappop(pq)
    print(ans)


operate()
