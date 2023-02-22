import sys
from collections import deque
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
k = [list(map(int, Input().rstrip())) for _ in range(rows)]
visited = [[[sys.maxsize] * cols for _ in range(rows)] for _ in range(2)]


def bfs():
    if rows == 1 and cols == 1:
        print(1)
        return
    qu = deque()
    qu.append((0, 0, False))  # row, col, broken
    visited[False][0][0] = visited[True][0][0] = 1

    depth = 2
    while qu:
        sz_qu = len(qu)
        for _ in range(sz_qu):
            cx, cy, status = qu.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if nx == rows - 1 and ny == cols - 1:
                    print(depth)
                    return
                if 0 <= nx < rows and 0 <= ny < cols:
                    if k[nx][ny] == 0:  # empty
                        if visited[status][nx][ny] == sys.maxsize:
                            visited[status][nx][ny] = depth
                            qu.append((nx, ny, status))
                    else:  # wall
                        if status:
                            continue
                        if visited[True][nx][ny] == sys.maxsize:
                            visited[True][nx][ny] = depth
                            qu.append((nx, ny, True))
        depth += 1
    print(-1)


def operate():
    visited[0][0][0] = visited[1][0][0] = 1
    bfs()


operate()
