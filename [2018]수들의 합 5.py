import sys
input = sys.stdin.readline
target = int(input())
left = 1
right = 1
sum = 1
ans = 0

while right <= target:
    if sum == target:
       ans += 1

    if sum <= target:
        right += 1
        sum += right
    else:
        sum -= left
        left += 1

print(ans)