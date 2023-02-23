import sys
from collections import deque
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]
sx, sy = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    global sx, sy
    for i in range(sz):
        try:
            sy = k[i].index(9)
            sx = i
            k[sx][sy] = 0
            return
        except ValueError:
            continue


def bfs(shark_sz):
    qu = deque()
    visited = [[False] * sz for _ in range(sz)]
    qu.append((sx, sy))
    visited[sx][sy] = True

    ax, ay = sys.maxsize, sys.maxsize
    t = 0
    while qu and ax == sys.maxsize:
        len_qu = len(qu)
        for _ in range(len_qu):
            cx, cy = qu.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < sz and 0 <= ny < sz and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if k[nx][ny] > shark_sz:
                        continue
                    elif k[nx][ny] == 0 or k[nx][ny] == shark_sz:
                        qu.append((nx, ny))
                    else:
                        if ax > nx or (ax == nx and ay > ny):
                            ax, ay = nx, ny
        t += 1
    return ax, ay, t


def operate():
    global sx, sy
    shark_sz = 2
    fish_eaten = 0
    sum_t = 0

    while True:
        nx, ny, t = bfs(shark_sz)
        if nx == sys.maxsize:  # no fish left to eat
            break
        k[nx][ny] = 0
        sx, sy = nx, ny
        sum_t += t
        fish_eaten += 1
        if fish_eaten == shark_sz:
            shark_sz += 1
            fish_eaten = 0
    print(sum_t)


initialize()
operate()
