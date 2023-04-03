import sys
from collections import deque
Input = sys.stdin.readline
rows, cols, lim = map(int, Input().split())
k = [Input().rstrip() for _ in range(rows)]
visited = [[[False] * (lim + 1) for _ in range(cols)] for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def bfs():
    qu = deque()
    qu.append([0, 0, 0])  # row, col, break
    visited[0][0][0] = True

    ans = 1
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cx, cy, cd = qu.popleft()
            if cx == rows - 1 and cy == cols - 1:
                print(ans)
                return
            for i in range(4):
                nx, ny, nd = cx + dx[i], cy + dy[i], cd
                if 0 <= nx < rows and 0 <= ny < cols:
                    if k[nx][ny] == '1':
                        nd += 1
                    if nd <= lim and not visited[nx][ny][nd]:
                        visited[nx][ny][nd] = True
                        qu.append([nx, ny, nd])
        ans += 1
    print(-1)
    return


bfs()
