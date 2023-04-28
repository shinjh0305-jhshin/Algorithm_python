import sys
from collections import deque
Input = sys.stdin.readline
cols, rows = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
room_idx = [[0] * cols for _ in range(rows)]
room_sz = {}
rooms = 1


def initialize():
    global rooms
    for i in range(rows):
        for j in range(cols):
            if room_idx[i][j] == 0:
                ret = make_room(i, j)
                room_sz[rooms] = ret
                rooms += 1


def make_room(x, y):
    sz = 1
    qu = deque([[x, y]])
    room_idx[x][y] = rooms
    while qu:
        cx, cy = qu.popleft()
        nxy = can_visit(cx, cy)
        for nx, ny in nxy:
            if room_idx[nx][ny] == 0:
                qu.append([nx, ny])
                room_idx[nx][ny] = rooms
                sz += 1
    return sz


def can_visit(cx, cy):
    num = k[cx][cy]
    res = []
    for i in range(4):
        if not num & (1 << i):
            res.append([cx + dx[i], cy + dy[i]])
    return res


def operate():
    merged_max = 0
    for x in range(rows):
        for y in range(cols):
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < rows and 0 <= ny < cols:
                    if room_idx[x][y] != room_idx[nx][ny]:
                        merged_max = max(merged_max, room_sz[room_idx[x][y]] + room_sz[room_idx[nx][ny]])
    print(rooms - 1, max(room_sz.values()), merged_max, sep='\n')


initialize()
operate()
