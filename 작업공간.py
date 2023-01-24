# Input redirection을 위한 작업공간
import sys
from collections import deque
from heapq import heappush, heappop
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
graph = [[] for _ in range(rows)]
for i in range(rows):
    graph[i] = list(map(int, Input().split()))
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
island = [[] for _ in range(6)]  # 같은 섬에 속하는 좌표들
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


def build_bridge(row, col, dir):
    depth = 0
    cur = graph[row][col]
    qu = deque()

    for _ in range(4):

    # island에 섬 좌표가 들어가 있다
    # operate에서 각 좌표를 하나씩 꺼내서 여기에 주면
    # 여기서는 그 방향으로 얼마나 갈 수 있는지를 판단해서
    # 새로운 pq를 하나 만들어서 (섬, 섬, 거리) 넣고
    # union find 진행한다




def operate():
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] and not visited[i][j]:
                group_island(i, j)
    a = 50


operate()
