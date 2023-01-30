import sys
Input = sys.stdin.readline
colors = int(Input())
rawdata = list(map(int, Input().split()))
target = int(Input())
ans = 0
for i in rawdata:
    if i < target:
        continue
    tmp = 1
    total = sum(rawdata)
    for _ in range(target):
        tmp *= i / total
        i -= 1
        total -= 1
    ans += tmp
print(ans)