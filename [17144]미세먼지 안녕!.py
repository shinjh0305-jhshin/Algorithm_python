import sys
Input = sys.stdin.readline
rows, cols, t = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for i in range(rows):
    if k[i][0] == -1:
        cleaner_row = i
        break


def spread():
    global k
    tmp = [[0] * cols for _ in range(rows)]
    tmp[cleaner_row][0] = tmp[cleaner_row + 1][0] = -1
    for i in range(rows):
        for j in range(cols):
            if k[i][j] > 0:
                spreaded = 0
                dust = k[i][j] // 5
                for l in range(4):
                    nx, ny = i + dx[l], j + dy[l]
                    if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] != -1:
                        tmp[nx][ny] += dust
                        spreaded += 1
                tmp[i][j] += k[i][j] - dust * spreaded
    k = tmp


def circulate():
    for i in range(cleaner_row - 2, -1, -1):
        k[i + 1][0] = k[i][0]
    for j in range(1, cols):
        k[0][j - 1] = k[0][j]
    for i in range(1, cleaner_row + 1):
        k[i - 1][cols - 1] = k[i][cols - 1]
    for j in range(cols - 2, 0, -1):
        k[cleaner_row][j + 1] = k[cleaner_row][j]
    k[cleaner_row][1] = 0

    for i in range(cleaner_row + 3, rows):
        k[i - 1][0] = k[i][0]
    for j in range(1, cols):
        k[rows - 1][j - 1] = k[rows - 1][j]
    for i in range(rows - 2, cleaner_row, -1):
        k[i + 1][cols - 1] = k[i][cols - 1]
    for j in range(cols - 2, 0, -1):
        k[cleaner_row + 1][j + 1] = k[cleaner_row + 1][j]
    k[cleaner_row + 1][1] = 0


def operate():
    for _ in range(t):
        spread()
        circulate()
    ans = 0
    for i in range(rows):
        ans += sum(k[i])
    ans += 2
    print(ans)


operate()