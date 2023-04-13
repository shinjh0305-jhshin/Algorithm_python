import sys
Input = sys.stdin.readline
sz, target = map(int, Input().split())
k = list(map(int, Input().split()))


def operate():
    left, right = 0, max(k)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        res = 0
        for x in k:
            if x - mid > 0:
                res += x - mid
        if res >= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)


operate()
