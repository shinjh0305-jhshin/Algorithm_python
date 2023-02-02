import sys
from collections import deque
from itertools import combinations
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
graph = []
for _ in range(rows):
    graph.append(list(map(int, Input().split())))
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
blanks = []  # 빈 공간의 index
viruses = []  # 바이러스의 index


def initialize():
    global v
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 0:
                blanks.append([i, j])
            elif graph[i][j] == 2:
                viruses.append([i, j])


def invert_area(k, to):
    for i in k:
        graph[i[0]][i[1]] = to


def bfs():
    global rows, cols
    visited = [[False] * cols for _ in range(rows)]
    for x in viruses:
        visited[x[0]][x[1]] = True
    qu = deque(viruses)
    zeros = len(blanks) - 3
    while qu:
        c = qu.pop()
        for i in range(4):
            nr = c[0] + dx[i]
            nc = c[1] + dy[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                if graph[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    qu.append([nr, nc])
                    zeros -= 1
    return zeros


def operate():
    ans = -sys.maxsize
    for new_wall in combinations(blanks, 3):
        invert_area(new_wall, 1)  # 벽으로 바꾸기
        ans = max(ans, bfs())
        invert_area(new_wall, 0)  # 빈 칸으로 바꾸기
    print(ans)


initialize()
operate()