import sys
from collections import deque
from itertools import combinations
Input = sys.stdin.readline
sz, target = map(int, Input().split())
graph = [list(map(int, Input().split())) for _ in range(sz)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
blanks = 0
virus = []


def initialize():
    global blanks
    for i in range(sz):
        for j in range(sz):
            if graph[i][j] == 0:
                blanks += 1
            elif graph[i][j] == 2:
                virus.append([i, j])


def spread_virus(v):
    visited = [[False] * sz for _ in range(sz)]
    left_blanks = blanks
    qu = deque(v)
    for r, c in v:
        visited[r][c] = True

    ans = 0
    while qu:
        if left_blanks == 0:
            return ans
        it = len(qu)
        for _ in range(it):
            cr, cc = qu.popleft()
            for i in range(4):
                nr, nc = cr + dx[i], cc + dy[i]
                if 0 <= nr < sz and 0 <= nc < sz and not visited[nr][nc] and graph[nr][nc] != 1:
                    visited[nr][nc] = True
                    qu.append([nr, nc])
                    if graph[nr][nc] == 0:
                        left_blanks -= 1
        ans += 1

    return sys.maxsize


def operate():
    ans = sys.maxsize
    for tmp_virus in combinations(virus, target):
        ans = min(ans, spread_virus(tmp_virus))
    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)


initialize()
operate()
