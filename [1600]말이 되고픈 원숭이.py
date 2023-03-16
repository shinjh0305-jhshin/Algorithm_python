import sys
from collections import deque
Input = sys.stdin.readline
horses = int(Input())
cols, rows = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dhx, dhy = [2, 1, -1, -2, -2, -1, 1, 2], [-1, -2, -2, -1, 1, 2, 2, 1]
visited = [[[False] * (horses + 1) for _ in range(cols)] for _ in range(rows)]


def operate():
    qu = deque()
    qu.append([0, 0, 0])

    mov = 0
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cx, cy, ch = qu.popleft()
            if cx == rows - 1 and cy == cols - 1:
                print(mov)
                return

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] == 0:
                    if not visited[nx][ny][ch]:
                        visited[nx][ny][ch] = True
                        qu.append([nx, ny, ch])

            if ch < horses:
                for i in range(8):
                    nx, ny = cx + dhx[i], cy + dhy[i]
                    if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] == 0:
                        if not visited[nx][ny][ch + 1]:
                            visited[nx][ny][ch + 1] = True
                            qu.append([nx, ny, ch + 1])
        mov += 1

    print(-1)


operate()

