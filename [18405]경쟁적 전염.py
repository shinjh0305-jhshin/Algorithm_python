import sys
from collections import deque
Input = sys.stdin.readline
sz, viruses = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
v = [deque() for _ in range(viruses + 1)]  # 바이러스가 있는 index
t, x, y = map(int, Input().split())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    for i in range(sz):
        for j in range(sz):
            if k[i][j]:
                v[k[i][j]].append([i, j])


def spread_virus():
    for i in range(1, viruses + 1):
        len_qu = len(v[i])
        for _ in range(len_qu):
            cx, cy = v[i].popleft()
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < sz and 0 <= ny < sz and not k[nx][ny]:
                    k[nx][ny] = i
                    v[i].append([nx, ny])


def operate():
    for _ in range(t):
        spread_virus()
    print(k[x - 1][y - 1])


initialize()
operate()