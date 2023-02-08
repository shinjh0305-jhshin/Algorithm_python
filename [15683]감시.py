import sys
from copy import deepcopy
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
graph = [list(map(int, Input().split())) for _ in range(rows)]
cctv = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
ans = sys.maxsize


def initialize():
    for i in range(rows):
        for j in range(cols):
            if 1 <= graph[i][j] <= 5:
                cctv.append((i, j))


def mask_area(idx, d, tmp_graph):
    nx = cctv[idx][0] + dx[d]
    ny = cctv[idx][1] + dy[d]

    while 0 <= nx < rows and 0 <= ny < cols and tmp_graph[nx][ny] != 6:
        if tmp_graph[nx][ny] == 0:
            tmp_graph[nx][ny] = -1
        nx += dx[d]
        ny += dy[d]


def install_cctv(idx, tmp_graph):
    if idx == len(cctv):
        global ans
        tmp = 0
        for i in range(rows):
            for j in range(cols):
                if tmp_graph[i][j] == 0:
                    tmp += 1
        ans = min(ans, tmp)
        return
    cctv_type = graph[cctv[idx][0]][cctv[idx][1]]
    if cctv_type == 1:
        for i in range(4):
            next_graph = deepcopy(tmp_graph)
            mask_area(idx, i, next_graph)
            install_cctv(idx + 1, next_graph)
    elif cctv_type == 2:
        for i in range(2):
            next_graph = deepcopy(tmp_graph)
            mask_area(idx, i, next_graph)
            mask_area(idx, i + 2, next_graph)
            install_cctv(idx + 1, next_graph)
    elif cctv_type == 3:
        for i in range(4):
            next_graph = deepcopy(tmp_graph)
            mask_area(idx, i, next_graph)
            mask_area(idx, (i + 1) % 4, next_graph)
            install_cctv(idx + 1, next_graph)
    elif cctv_type == 4:
        for i in range(4):
            next_graph = deepcopy(tmp_graph)
            mask_area(idx, i, next_graph)
            mask_area(idx, (i + 1) % 4, next_graph)
            mask_area(idx, (i + 2) % 4, next_graph)
            install_cctv(idx + 1, next_graph)
    elif cctv_type == 5:
        next_graph = deepcopy(tmp_graph)
        for i in range(4):
            mask_area(idx, i, next_graph)
        install_cctv(idx + 1, next_graph)


initialize()
install_cctv(0, graph)
print(ans)