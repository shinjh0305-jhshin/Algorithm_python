import sys
from collections import deque

Input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
rows, cols = map(int, Input().split())
graph = [[0]]
visited = [[0] * (cols + 1) for _ in range(rows + 1)]

for i in range(1, rows + 1):
    graph.append([0] + list(map(int, input())))


def dfs():
    visited[1][1] = 1
    qu = deque()
    qu.append((1, 1))

    while qu:
        curNode = qu.popleft()
        for i in range(4):
            x = curNode[0] + dx[i]
            y = curNode[1] + dy[i]
            if 0 < x <= rows and 0 < y <= cols:
                if not visited[x][y] and graph[x][y]:
                    visited[x][y] = visited[curNode[0]][curNode[1]] + 1
                    qu.append((x, y))


dfs()
print(visited[rows][cols])