import sys
from collections import deque
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
graph = [Input().rstrip() for _ in range(rows)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(r, c):
    visited = [[False] * cols for _ in range(rows)]
    qu = deque()
    visited[r][c] = True
    qu.append((r, c))

    depth = -1
    while qu:
        it = len(qu)
        for _ in range(it):
            cr, cc = qu.popleft()
            for i in range(4):
                nr, nc = cr + dx[i], cc + dy[i]
                if 0 <= nr < rows and 0 <= nc < cols and graph[nr][nc] == 'L' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    qu.append((nr, nc))
        depth += 1
    return depth


def operate():
    ans = -sys.maxsize
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 'L':
                ans = max(ans, bfs(i, j))
    print(ans)


operate()
