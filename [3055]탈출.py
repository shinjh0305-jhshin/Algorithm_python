import sys
from collections import deque
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [list(Input().rstrip()) for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = [[False] * cols for _ in range(rows)]
water_qu, dochi_qu = deque(), deque()


def initialize():
    for i in range(rows):
        for j in range(cols):
            if k[i][j] == 'S':
                dochi_qu.append((i, j))
                visited[i][j] = True
                k[i][j] = '.'
            elif k[i][j] == '*':
                water_qu.append((i, j))


def spread_water():
    len_qu = len(water_qu)
    for _ in range(len_qu):
        x, y = water_qu.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] == '.':
                k[nx][ny] = '*'
                water_qu.append((nx, ny))
        water_qu.append((x, y))


def operate():
    ans = 1
    while dochi_qu:
        spread_water()
        len_qu = len(dochi_qu)
        for _ in range(len_qu):
            x, y = dochi_qu.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols:
                    if visited[nx][ny] or k[nx][ny] == '*' or k[nx][ny] == 'X':
                        continue
                    if k[nx][ny] == '.':
                        dochi_qu.append((nx, ny))
                        visited[nx][ny] = True
                    elif k[nx][ny] == 'D':
                        return ans
        ans += 1
    return 'KAKTUS'


initialize()
print(operate())
