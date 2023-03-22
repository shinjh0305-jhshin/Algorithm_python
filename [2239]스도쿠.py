import sys
k = [list(map(int, input().rstrip())) for _ in range(9)]
in_row, in_col, in_box = \
    [[False] * 10 for _ in range(9)], [[False] * 10 for _ in range(9)], [[False] * 10 for _ in range(9)]
zero = []


def dfs(idx=0):
    if idx == len(zero):
        return True
    for x in range(1, 10):
        r, c = zero[idx]
        if in_row[r][x] or in_col[c][x] or in_box[(r // 3) * 3 + (c // 3)][x]:
            continue

        in_row[r][x] = in_col[c][x] = in_box[(r // 3) * 3 + (c // 3)][x] = True

        if dfs(idx + 1):
            k[zero[idx][0]][zero[idx][1]] = x
            return True

        in_row[r][x] = in_col[c][x] = in_box[(r // 3) * 3 + (c // 3)][x] = False

    return False


def operate():
    for i in range(9):
        for j in range(9):
            if k[i][j] == 0:
                zero.append([i, j])
            else:
                in_row[i][k[i][j]] = True
                in_col[j][k[i][j]] = True
                in_box[(i // 3) * 3 + (j // 3)][k[i][j]] = True

    dfs()

    for i in range(9):
        print(*k[i], sep='')


operate()
