sz = int(input())
target = int(input())


def operate():
    left, right = 0, sz ** 2

    while left + 1 != right:
        mid = (left + right) // 2

        ans = 0
        for i in range(1, sz + 1):
            ans += min(mid // i, sz)

        if ans >= target:
            right = mid
        else:
            left = mid

    print(right)


operate()
