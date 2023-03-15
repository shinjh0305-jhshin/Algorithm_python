import sys
Input = sys.stdin.readline
rows, cols, sharks = map(int, Input().split())
field = [[[] for _ in range(cols + 1)] for _1 in range(rows + 1)]  # speed, direction, size
cur_shark = []


def initialize():
    for _ in range(sharks):
        r, c, s, d, z = map(int, Input().split())
        field[r][c].append([s, d, z])  # speed, direction, size
        cur_shark.append((r, c))


def move_shark():
    global cur_shark, field
    visited = [[False] * (cols + 1) for _ in range(rows + 1)]
    to_eat = []
    next_field = [[[] for _ in range(cols + 1)] for _1 in range(rows + 1)]  # speed, direction, size
    next_shark = []
    for x, y in cur_shark:
        if len(field[x][y]) <= 0:  # 잡힌 물고기
            continue
        ori_s, d, z = field[x][y][0]
        s = ori_s
        if 1 <= d <= 2:
            s %= (rows - 1) * 2
        else:
            s %= (cols - 1) * 2
        while s:
            if d == 1:
                mov = min(s, x - 1)
                x -= mov
            elif d == 2:
                mov = min(s, rows - x)
                x += mov
            elif d == 3:
                mov = min(s, cols - y)
                y += mov
            else:
                mov = min(s, y - 1)
                y -= mov
            s -= mov
            if s:
                if d % 2:
                    d += 1
                else:
                    d -= 1
        if visited[x][y]:
            to_eat.append([x, y])
        else:
            next_shark.append((x, y))
        visited[x][y] = True
        next_field[x][y].append([ori_s, d, z])

    for x, y in to_eat:
        next_field[x][y].sort(key=lambda t: t[2], reverse=True)
        del next_field[x][y][1:]

    field = next_field
    cur_shark = next_shark


def catch_fish(j):
    for i in range(1, rows + 1):
        if len(field[i][j]):
            ret = field[i][j].pop()
            return ret[2]
    return 0


def operate():
    ans = 0
    for i in range(1, cols + 1):
        ans += catch_fish(i)
        move_shark()
    print(ans)


initialize()
operate()
