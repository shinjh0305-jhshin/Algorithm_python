import sys
from collections import deque
Input = sys.stdin.readline

bldgs = int(Input())
prevBldgs = [0 for _ in range(bldgs + 1)]
order = [[] for _ in range(bldgs + 1)]
duration = [0 for _ in range(bldgs + 1)]
result = [0 for _ in range(bldgs + 1)]

for i in range(1, bldgs + 1):
    tmp = list(map(int, Input().split()))
    duration[i] = tmp[0]
    for j in tmp[1:-1]:
        prevBldgs[i] += 1
        order[j].append(i)

qu = deque()
for i in range(1, bldgs + 1):
    if prevBldgs[i] == 0:
        result[i] = duration[i]
        qu.append(i)
while qu:
    curBldg = qu.popleft()
    for nextBldg in order[curBldg]:
        prevBldgs[nextBldg] -= 1
        result[nextBldg] = max(result[nextBldg], result[curBldg] + duration[nextBldg])
        if prevBldgs[nextBldg] == 0:
            qu.append(nextBldg)

print(*result[1:], sep='\n')