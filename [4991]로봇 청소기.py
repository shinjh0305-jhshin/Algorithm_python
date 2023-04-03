import sys
from collections import deque
Input = sys.stdin.readline
rows, cols, spots, ix, iy = 0, 0, 0, 0, 0
k, res = [], []
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    global rows, cols, spots, k, ix, iy
    cols, rows = map(int, Input().split())
    if not rows:
        return False
    k = [list(Input().rstrip()) for _ in range(rows)]
    spots = 0
    for i in range(rows):
        for j in range(cols):
            if k[i][j] == '*':
                k[i][j] = spots
                spots += 1
            elif k[i][j] == 'o':
                ix, iy = i, j
                k[ix][iy] = '.'
    return True


def operate():
    visited = [[[False] * (1 << spots) for _ in range(cols)] for _ in range(rows)]
    qu = deque()
    visited[ix][iy][0] = True
    qu.append([ix, iy, 0])

    ans = 0
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cx, cy, ch = qu.popleft()
            if ch == (1 << spots) - 1:
                return ans
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny][ch] and k[nx][ny] != 'x':
                    if k[nx][ny] == '.':
                        visited[nx][ny][ch] = True
                        qu.append([nx, ny, ch])
                    else:
                        idx = k[nx][ny]
                        nh = ch | (1 << idx)
                        visited[nx][ny][nh] = True
                        qu.append([nx, ny, nh])
        ans += 1
    return -1


while True:
    flag = initialize()
    if not flag:
        break
    res.append(operate())

print(*res, sep='\n')
