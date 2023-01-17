import sys
from heapq import heappop, heappush, heapify
Input = sys.stdin.readline
sz = int(Input())
rawdata = []
for _ in range(sz):
    rawdata.append(int(Input()))
heapify(rawdata)

ans = 0
while len(rawdata) > 1:
    sumOfTwo = 0
    sumOfTwo += heappop(rawdata)
    sumOfTwo += heappop(rawdata)
    ans += sumOfTwo
    heappush(rawdata, sumOfTwo)

print(ans)