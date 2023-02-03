import sys
from collections import deque
Input = sys.stdin.readline
cols, rows = map(int, Input().split())
graph = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
qu = deque()  # 다 익은 토마토가 들어 있는 곳
not_ripen = 0  # 안 익은 토마토의 개수


def initialize():
    global not_ripen
    for _ in range(rows):
        graph.append(list(map(int, Input().split())))

    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 0:
                not_ripen += 1
            elif graph[i][j] == 1:
                qu.append([i, j])


def bfs():
    global not_ripen
    if not_ripen == 0:  # 처음부터 다 익은 상태
        print(0)
        return
    days = 0
    while qu:
        sz = len(qu)
        for _ in range(sz):
            cx, cy = qu.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] == 0:
                    qu.append([nx, ny])
                    not_ripen -= 1
                    graph[nx][ny] = 1
        days += 1
    if not_ripen == 0:
        print(days - 1)
    else:
        print(-1)


initialize()
bfs()
