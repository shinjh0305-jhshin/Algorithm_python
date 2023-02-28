import sys
from collections import deque
Input = sys.stdin.readline
tc = int(Input())
dx, dy = [2, 1, -1, -2, -2, -1, 1, 2], [-1, -2, -2, -1, 1, 2, 2, 1]


def operate():
    sz = int(Input())
    sx, sy = map(int, Input().split())
    ex, ey = map(int, Input().split())

    if sx == ex and sy == ey:
        print(0)
        return

    qu = deque()
    visited = [[False] * sz for _ in range(sz)]
    qu.append([sx, sy])

    it = 1
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cx, cy = qu.popleft()
            for i in range(8):
                nx, ny = cx + dx[i], cy + dy[i]
                if nx == ex and ny == ey:
                    print(it)
                    return
                if 0 <= nx < sz and 0 <= ny < sz and not visited[nx][ny]:
                    visited[nx][ny] = True
                    qu.append([nx, ny])
        it += 1


for _ in range(tc):
    operate()
