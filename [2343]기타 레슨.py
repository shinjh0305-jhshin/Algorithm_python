lesson, disk = map(int, input().split())
rawdata = list(map(int, input().split()))

left = max(rawdata)
right = sum(rawdata)

while left <= right:
    mid = int((left + right) / 2)
    ans = 0
    length = 0
    for i in rawdata:
        if length + i > mid:
            ans += 1
            length = i
        else:
            length += i
    if length:
        ans += 1

    if ans > disk:
        left = mid + 1
    else:
        right = mid - 1

print(left)