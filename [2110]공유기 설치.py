import sys
Input = sys.stdin.readline
sz, target = map(int, Input().split())
k = [int(Input()) for _ in range(sz)]


def operate():
    k.sort()
    left, right = 1, (k[-1] - k[0]) // (target - 1) + 1

    while left + 1 != right:
        mid = (left + right) // 2

        prev_pos, cnt = k[0], 1

        flag = False
        for x in k:
            if x - prev_pos >= mid:
                prev_pos, cnt = x, cnt + 1
            if cnt == target:
                flag = True
                break

        if flag:
            left = mid
        else:
            right = mid

    print(left)


operate()