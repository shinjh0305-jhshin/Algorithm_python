import sys
from heapq import heappush, heappop
sz, max_bk = map(int, input().split())
k = list(map(int, input().split()))
plus, minus = [], []


def operate():
    for x in k:
        if x > 0:
            heappush(plus, -x)
        else:
            heappush(minus, x)

    # 마지막 끝나는 장소까지의 거리는 나중에 한 번 빼준다
    finish_dist = -sys.maxsize
    if plus:
        finish_dist = max(finish_dist, -plus[0])
    if minus:
        finish_dist = max(finish_dist, -minus[0])

    ans = 0
    while plus:
        ans -= heappop(plus) * 2
        for _ in range(max_bk - 1):
            if not plus:
                break
            heappop(plus)
    while minus:
        ans -= heappop(minus) * 2
        for _ in range(max_bk - 1):
            if not minus:
                break
            heappop(minus)
    ans -= finish_dist
    print(ans)


operate()
