import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
sz, L, R = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
visited = [[False] * sz for _ in range(sz)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
qu = deque()


def dfs(cx, cy):
    visited[cx][cy] = True
    qu.append([cx, cy])
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < sz and 0 <= ny < sz:
            if not visited[nx][ny] and L <= abs(k[nx][ny] - k[cx][cy]) <= R:
                dfs(nx, ny)


def move():
    total = sum(list(map(lambda x: k[x[0]][x[1]], qu)))
    ppl = total // len(qu)

    while qu:
        x, y = qu.pop()
        k[x][y] = ppl


def operate():
    ans = 0
    while True:
        global visited
        moved = False
        for i in range(sz):
            for j in range(sz):
                if not visited[i][j]:
                    dfs(i, j)
                    if len(qu) > 1:
                        moved = True
                        move()
                    else:
                        qu.clear()
        if not moved:
            break
        visited = [[False] * sz for _ in range(sz)]
        ans += 1
    print(ans)


operate()