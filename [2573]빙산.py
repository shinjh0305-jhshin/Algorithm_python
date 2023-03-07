import sys
from collections import deque
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
qu = deque()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    for i in range(rows):
        for j in range(cols):
            if k[i][j]:
                qu.append((i, j))


def connected():
    ices = len(qu) - 1
    visited = [[False] * cols for _ in range(rows)]
    q = deque([qu[0]])
    visited[qu[0][0]][qu[0][1]] = True
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and k[nx][ny]:
                ices -= 1
                visited[nx][ny] = True
                q.append((nx, ny))
    if ices:
        return False
    else:
        return True


def melt():
    global k
    tmp = [x[:] for x in k]
    len_qu = len(qu)
    for _ in range(len_qu):
        cx, cy = qu.popleft()
        ice = tmp[cx][cy]
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] == 0:
                    ice -= 1
        if ice <= 0:
            tmp[cx][cy] = 0
        else:
            tmp[cx][cy] = ice
            qu.append((cx, cy))
    k = tmp


def operate():
    ans = 0
    while True:
        if len(qu) == 0:
            print(0)
            return
        if not connected():
            break
        melt()
        ans += 1
    print(ans)


initialize()
operate()

