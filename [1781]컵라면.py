import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
sz = int(Input())
k = [tuple(map(int, Input().split())) for _ in range(sz)]
k.sort(key=lambda x: x[0], reverse=True)  # x[1]은 정렬 대상이 아님을 명시


def operate():
    idx = 0
    ans = 0
    pq = []
    for t in range(k[0][0], 0, -1):
        while idx < sz and k[idx][0] >= t:
            heappush(pq, -k[idx][1])
            idx += 1
        if pq:
            ans -= heappop(pq)
    print(ans)


operate()
