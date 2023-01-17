import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
sz = int(Input())
minusHeap = []
plusHeap = []
zeros = 0
ones = 0
for _ in range(sz):
    temp = int(Input())
    if temp < 0:
        heappush(minusHeap, temp)
    elif temp > 0:
        if temp == 1:
            ones += 1
        else:
            heappush(plusHeap, -temp)
    elif temp == 0:
        zeros += 1
ans = 0

def pairNum(qu):
    global ans
    while len(qu) > 1:
        tmp = heappop(qu)
        tmp *= heappop(qu)
        ans += tmp
    if len(qu) == 1:
        tmp = heappop(qu)
        if qu is minusHeap and not zeros:
            ans += tmp
        elif qu is plusHeap:
            ans += tmp * -1


pairNum(plusHeap)
pairNum(minusHeap)
ans += ones
print(ans)