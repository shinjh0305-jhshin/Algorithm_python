import sys
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]


def make_map(i, j, d1, d2):
    ans = [0] * 6
    ly, ry = j, j
    dly, dry = -1, 1
    for x in range(sz):
        for y in range(sz):
            if x < i:
                if y <= j:
                    ans[1] += k[x][y]
                else:
                    ans[2] += k[x][y]
            elif x > i + d1 + d2:
                if y < j - d1 + d2:
                    ans[3] += k[x][y]
                else:
                    ans[4] += k[x][y]
            else:
                if y < ly:
                    if x < i + d1:
                        ans[1] += k[x][y]
                    else:
                        ans[3] += k[x][y]
                elif ly <= y <= ry:
                    ans[5] += k[x][y]
                else:
                    if x <= i + d2:
                        ans[2] += k[x][y]
                    else:
                        ans[4] += k[x][y]
        if x == i + d1:
            dly = 1
        if x == i + d2:
            dry = -1
        if i <= x < i + d1 + d2:
            ly += dly
            ry += dry
    ans = ans[1:]
    return max(ans) - min(ans)


def operate():
    ans = sys.maxsize
    for i in range(sz):
        for j in range(sz):
            for d1 in range(1, sz):
                for d2 in range(1, sz):
                    if i + d1 + d2 > sz - 1 or d1 > j or j > sz - d2 - 1:
                        continue
                    ans = min(ans, make_map(i, j, d1, d2))
    print(ans)


operate()
