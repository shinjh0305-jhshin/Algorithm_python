import sys
from collections import deque
from heapq import heappush, heappop
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
graph = [[] for _ in range(rows)]
for k in range(rows):
    graph[k] = list(map(int, Input().split()))
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
island = [[] for _ in range(7)]  # 같은 섬에 속하는 좌표들
island_to_island = [] # 섬에서 섬까지 거리 (dist, start, end)
root = [-1] * 7
visited = [[False] * cols for _ in range(rows)]
islands = 0


def group_island(row, col):
    global islands
    qu = deque()
    qu.append((row, col))
    visited[row][col] = True
    island[islands].append((row, col))

    while qu:
        x, y = qu.popleft()
        graph[x][y] = islands + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                qu.append((nx, ny))
                island[islands].append((nx, ny))
    islands += 1


def build_bridge(row, col):
    qu = deque()
    for i in range(4):
        qu.append((row, col, i))

    length = 0
    while qu:
        sz_qu = len(qu)
        for _ in range(sz_qu):
            x, y, d = qu.popleft()
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < rows and 0 <= ny < cols:
                if graph[nx][ny] == 0:  # sea
                    qu.append((nx, ny, d))
                elif graph[nx][ny] != graph[row][col] and length >= 2:
                    heappush(island_to_island, (length, graph[row][col], graph[nx][ny]))
        length += 1


def find(a):
    if root[a] < 0:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False
    if root_a > root_b:
        root_a, root_b = root_b, root_a
    root[root_a] += root[root_b]
    root[root_b] = root_a
    return True


def operate():
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] and not visited[i][j]:
                group_island(i, j)

    for i in range(1, islands + 1):
        for row, col in island[i]:
            build_bridge(row, col)

    bridges = 0
    ans = 0
    while bridges != islands - 1:
        if not island_to_island:
            print(-1)
            return
        d, x, y = heappop(island_to_island)
        if union(x, y):
            ans += d
            bridges += 1
    print(ans)


operate()