import sys
Input = sys.stdin.readline
sz = int(Input())
rawdata = []
for _ in range(sz):
    start, end = map(int, Input().split());
    rawdata.append((start, end))
rawdata.sort(reverse=True)

target = rawdata[0][0]
ans = 1
for mov in rawdata[1:]:
    if mov[1] <= target:
        target = mov[0]
        ans += 1
print(ans)