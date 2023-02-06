import sys
from collections import deque
from itertools import combinations
Input = sys.stdin.readline
nodes, shops = map(int, Input().split())
graph = []
shop = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
houses = 0


def initialize():
    global houses
    for _ in range(nodes):
        graph.append(list(map(int, Input().split())))
    for i in range(nodes):
        for j in range(nodes):
            if graph[i][j] == 2:
                shop.append([i, j])
            elif graph[i][j] == 1:
                houses += 1


def bfs(t):
    left_houses = houses
    visited = [[False] * nodes for _ in range(nodes)]
    qu = deque(t)
    dist = 1
    ans = 0
    for i, j in qu:
        visited[i][j] = True
    while left_houses:
        sz_qu = len(qu)
        for _ in range(sz_qu):
            cx, cy = qu.popleft()
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < nodes and 0 <= ny < nodes and not visited[nx][ny]:
                    visited[nx][ny] = True
                    qu.append([nx, ny])
                    if graph[nx][ny] == 1:
                        left_houses -= 1
                        ans += dist
        dist += 1
    return ans


def operate():
    ans = sys.maxsize
    for tmp in combinations(shop, shops):
        ans = min(ans, bfs(tmp))
    print(ans)


initialize()
operate()
