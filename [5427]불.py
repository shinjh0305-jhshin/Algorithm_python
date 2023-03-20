import sys
from collections import deque
Input = sys.stdin.readline
tc = int(Input())
rows, cols = 0, 0
new_fire = []  # 직전 시각에 처음으로 불이 번진 곳
k = []
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    global rows, cols, k
    cols, rows = map(int, Input().split())
    k = [list(Input().rstrip()) for _ in range(rows)]
    new_fire.clear()
    x, y = 0, 0

    for i in range(rows):
        for j in range(cols):
            if k[i][j] == '@':
                k[i][j] = '.'
                x, y = i, j
            elif k[i][j] == '*':
                new_fire.append([i, j])
    return x, y


def move_fire():
    global new_fire
    new_new_fire = []

    for x, y in new_fire:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] == '.':
                new_new_fire.append([nx, ny])
                k[nx][ny] = '*'

    new_fire = new_new_fire


def operate():
    cx, cy = initialize()
    qu = deque([[cx, cy]])
    visited = [[False] * cols for _ in range(rows)]
    visited[cx][cy] = True
    ans = 1

    while qu:
        move_fire()
        len_qu = len(qu)

        for _ in range(len_qu):
            cx, cy = qu.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if not (0 <= nx < rows and 0 <= ny < cols):
                    print(ans)
                    return
                if k[nx][ny] == '.' and not visited[nx][ny]:
                    qu.append([nx, ny])
                    visited[nx][ny] = True
        ans += 1
    print("IMPOSSIBLE")


for _ in range(tc):
    operate()
