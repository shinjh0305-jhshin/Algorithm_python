import sys
Input = sys.stdin.readline
sz, length = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
installed = [[False] * sz for _ in range(sz)]


def check_row(i):
    prev_h = k[i][0]
    j = 1
    while j < sz:
        if k[i][j] > prev_h:
            if k[i][j] - prev_h != 1 or j < length:
                return False
            for pj in range(j - 1, j - length - 1, -1):
                if k[i][pj] != prev_h or installed[i][pj]:
                    return False
            for pj in range(j - 1, j - length - 1, -1):
                installed[i][pj] = True
            prev_h = k[i][j]
        elif k[i][j] < prev_h:
            if prev_h - k[i][j] != 1 or j > sz - length:
                return False
            for nj in range(j, j + length):
                if k[i][nj] != prev_h - 1 or installed[i][nj]:
                    return False
            for nj in range(j, j + length):
                installed[i][nj] = True
            prev_h = k[i][j]
            j += length - 1
        j += 1
    return True


def check_col(j):
    prev_h = k[0][j]
    i = 1
    while i < sz:
        if k[i][j] > prev_h:
            if k[i][j] - prev_h != 1 or i < length:
                return False
            for pi in range(i - 1, i - length - 1, -1):
                if k[pi][j] != prev_h or installed[pi][j]:
                    return False
            for pi in range(i - 1, i - length - 1, -1):
                installed[pi][j] = True
            prev_h = k[i][j]
        elif k[i][j] < prev_h:
            if prev_h - k[i][j] != 1 or i > sz - length:
                return False
            for ni in range(i, i + length):
                if k[ni][j] != prev_h - 1 or installed[ni][j]:
                    return False
            for ni in range(i, i + length):
                installed[ni][j] = True
            prev_h = k[i][j]
            i += length - 1
        i += 1
    return True


def operate():
    ans = 0
    for i in range(sz):
        if check_row(i):
            ans += 1

    global installed
    installed = [[False] * sz for _ in range(sz)]

    for j in range(sz):
        if check_col(j):
            ans += 1
    print(ans)


operate()
