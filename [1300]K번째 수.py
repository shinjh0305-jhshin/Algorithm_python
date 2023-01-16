sz = int(input())
target = int(input())
left = 1
right = target
ans = 0

while left <= right:
    mid = int((left + right) / 2)
    cnt = 0
    for i in range(1, sz + 1):
        cnt += min(int(mid / i), sz)
    if cnt >= target:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)