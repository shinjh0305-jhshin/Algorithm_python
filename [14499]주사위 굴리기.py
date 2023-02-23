import sys
Input = sys.stdin.readline
rows, cols, cx, cy, ops = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
op = list(map(int, Input().split()))
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
ns, ew = [6, 5, 1, 2], [6, 3, 1, 4]
dice = [0] * 7


def rotate(code):
    if code <= 2:
        target = ew
    else:
        target = ns

    tmp_dice = dice[:]
    if code % 2 == 0:  # 서남
        for i in range(4):
            dice[target[i]] = tmp_dice[target[(i - 1) % 4]]
    else:
        for i in range(4):  # 동북
            dice[target[i]] = tmp_dice[target[(i + 1) % 4]]


def mov():
    ans = []
    global cx, cy
    for i in op:
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < rows and 0 <= ny < cols:
            rotate(i)
            if k[nx][ny] == 0:
                k[nx][ny] = dice[6]
            else:
                dice[6] = k[nx][ny]
                k[nx][ny] = 0
            ans.append(dice[1])
            cx, cy = nx, ny
    print(*ans, sep='\n')


mov()
