import sys
from collections import deque
Input = sys.stdin.readline
sz = int(Input())
apples = int(Input())
k = [[0] * sz for _ in range(sz)]  # -1 : 뱀, 0 : 빈칸, 1 : 사과
rotate = []
sz_rotate = 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


def initialize():
    for _ in range(apples):
        x, y = map(int, Input().split())
        k[x - 1][y - 1] = 1

    global rotate, sz_rotate
    sz_rotate = int(Input())
    rotate = [list(Input().split()) for _ in range(sz_rotate)]


def operate():
    qu = deque()
    qu.append((0, 0))
    k[0][0] = -1
    cd = 0
    rotate_idx = 0

    ans = 1
    while True:
        cx, cy = qu[-1]
        nx, ny = cx + dx[cd], cy + dy[cd]

        if not (0 <= nx < sz and 0 <= ny < sz) or k[nx][ny] == -1:
            break
        if k[nx][ny] == 0:
            tx, ty = qu.popleft()
            k[tx][ty] = 0

        k[nx][ny] = -1
        qu.append((nx, ny))

        if rotate_idx < sz_rotate and ans == int(rotate[rotate_idx][0]):
            if rotate[rotate_idx][1] == 'D':
                cd = (cd - 1) % 4
            else:
                cd = (cd + 1) % 4
            rotate_idx += 1
        ans += 1
    print(ans)


initialize()
operate()
