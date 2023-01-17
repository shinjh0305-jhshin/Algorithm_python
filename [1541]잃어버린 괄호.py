import sys
Input = sys.stdin.readline
rawdata = Input()

ans = 0
tempSum = 0
curNum = 0
isMinus = False
for ch in rawdata:
    if ch.isdigit():
        curNum = curNum * 10 + int(ch)
    else:
        tempSum += curNum
        curNum = 0
        if ch == '-':
            if isMinus:
                ans -= tempSum
            else:
                ans += tempSum
                isMinus = True
            tempSum = 0
tempSum += curNum
if isMinus:
    ans -= tempSum
else:
    ans += tempSum
print(ans)

