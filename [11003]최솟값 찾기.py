import sys
from collections import deque

input = sys.stdin.readline

sz, block = map(int, input().split())
rawdata = list(map(int, input().split()))

dq = deque()

for i in range(sz):
    target = rawdata[i]
    while dq and dq[-1][0] > target:
        dq.pop()
    dq.append((target, i))
    if dq[0][1] <= i - block:
        dq.popleft()
    print(dq[0][0], end=' ')
