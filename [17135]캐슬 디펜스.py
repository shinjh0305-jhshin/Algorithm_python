import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
Input = sys.stdin.readline
rows, cols, d = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
dx = [0, -1, 0]
dy = [-1, 0, 1]
enemies = 0


def initialize():
    global enemies
    for i in range(rows):
        enemies += k[i].count(1)


def attack(row, col, graph):
    qu = deque()
    visited = [[False] * cols for _ in range(rows)]
    qu.append([row, col])

    enemy = []  # (y, x) : y를 기준으로 최솟값 찾기 위해 순서 바꿈
    distance = 1
    while qu and distance <= d and not enemy:
        it = len(qu)
        for _ in range(it):
            cx, cy = qu.popleft()
            for i in range(3):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 1:
                        enemy.append((ny, nx))
                    if not enemy:
                        qu.append([nx, ny])
        distance += 1
    if enemy:
        return min(enemy)
    else:
        return -1, -1


def play(archers):
    left_enemies = enemies
    tmp = deque(deepcopy(k))
    killed_enemies = 0
    while left_enemies:
        killed = []
        # 죽여야 하는 적들 찾아낸다
        for x in archers:
            killed.append(attack(rows, x, tmp))
        # 적들을 죽인다
        for y, x in killed:
            if x != -1 and tmp[x][y]:
                tmp[x][y] = 0
                left_enemies -= 1
                killed_enemies += 1
        # 한 칸씩 내린다
        left_enemies -= tmp[-1].count(1)
        tmp.pop()
        tmp.appendleft([0] * cols)
    return killed_enemies


def operate():
    ans = 0
    if enemies == 0:
        print(0)
        return
    for archers in combinations(range(0, cols), 3):
        ans = max(ans, play(archers))
    print(ans)


initialize()
operate()
