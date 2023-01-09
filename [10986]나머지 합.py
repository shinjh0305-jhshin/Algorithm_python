import sys
input = sys.stdin.readline
sz, divisor = map(int, input().split())
rawdata = list(map(int, input().split()))
divData = [0] * divisor;

curMod = 0
ans = 0
for num in rawdata:
    curMod = (curMod + num) % divisor
    if curMod == 0:
        ans += 1
    ans += divData[curMod]
    divData[curMod] += 1

print(ans)