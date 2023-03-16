import sys
from collections import deque
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
cheeses = 0


def initialize():
    global cheeses
    for i in range(rows):
        for j in range(cols):
            if k[i][j]:
                cheeses += 1


def operate():
    global cheeses
    ans = 0
    while cheeses:
        qu = deque([[0, 0]])
        visited = [[0] * cols for _ in range(rows)]
        visited[0][0] = True

        while qu:
            cx, cy = qu.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols:
                    if k[nx][ny] == 0:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            qu.append([nx, ny])
                    else:
                        visited[nx][ny] += 1

        for i in range(rows):
            for j in range(cols):
                if k[i][j] == 1 and visited[i][j] >= 2:
                    k[i][j] = 0
                    cheeses -= 1
        ans += 1
    print(ans)


initialize()
operate()


