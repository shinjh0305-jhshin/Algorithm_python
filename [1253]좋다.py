import sys
input = sys.stdin.readline
sz = int(input())
rawdata = list(map(int, input().split()))
rawdata.sort()

ans = 0
for x in range(sz):
    target = rawdata[x]
    left = 0
    right = sz - 1
    while left < right:
        sum = rawdata[left] + rawdata[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            if left == x:
                left += 1
            elif right == x:
                right -= 1
            else:
                ans += 1
                break
print(ans)
