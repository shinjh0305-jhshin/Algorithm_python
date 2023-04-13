import sys
Input = sys.stdin.readline
sz, target = map(int, input().split())
k = [int(Input()) for _ in range(sz)]


def operate():
    left, right = 1, max(k) + 1
    while left + 1 != right:
        mid = (left + right) // 2
        ans = 0
        for x in k:
            ans += x // mid
        if ans >= target:
            left = mid
        else:
            right = mid
    print(left)


operate()
