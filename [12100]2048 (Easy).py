import sys
from copy import deepcopy
Input = sys.stdin.readline
sz = int(Input())
rawdata = [list(map(int, Input().split())) for _ in range(sz)]
ans = -sys.maxsize


def move_up(graph):
    merged = [[False] * sz for _ in range(sz)]
    for j in range(sz):
        for i in range(1, sz):
            mov = i
            while mov > 0 and graph[mov - 1][j] == 0:
                mov -= 1
            if mov > 0 and graph[mov - 1][j] == graph[i][j] and not merged[mov - 1][j]:
                graph[mov - 1][j] *= 2
                graph[i][j] = 0
                merged[mov - 1][j] = True
            elif mov != i:
                graph[mov][j] = graph[i][j]
                graph[i][j] = 0
    return graph


def move_down(graph):
    merged = [[False] * sz for _ in range(sz)]
    for j in range(sz):
        for i in range(sz - 2, -1, -1):
            mov = i
            while mov < sz - 1 and graph[mov + 1][j] == 0:
                mov += 1
            if mov < sz - 1 and graph[mov + 1][j] == graph[i][j] and not merged[mov + 1][j]:
                graph[mov + 1][j] *= 2
                graph[i][j] = 0
                merged[mov + 1][j] = True
            elif mov != i:
                graph[mov][j] = graph[i][j]
                graph[i][j] = 0
    return graph


def move_left(graph):
    merged = [[False] * sz for _ in range(sz)]
    for i in range(sz):
        for j in range(1, sz):
            mov = j
            while mov > 0 and graph[i][mov - 1] == 0:
                mov -= 1
            if mov > 0 and graph[i][mov - 1] == graph[i][j] and not merged[i][mov - 1]:
                graph[i][mov - 1] *= 2
                graph[i][j] = 0
                merged[i][mov - 1] = True
            elif mov != j:
                graph[i][mov] = graph[i][j]
                graph[i][j] = 0
    return graph


def move_right(graph):
    merged = [[False] * sz for _ in range(sz)]
    for i in range(sz):
        for j in range(sz - 2, -1, -1):
            mov = j
            while mov < sz - 1 and graph[i][mov + 1] == 0:
                mov += 1
            if mov < sz - 1 and graph[i][mov + 1] == graph[i][j] and not merged[i][mov + 1]:
                graph[i][mov + 1] *= 2
                graph[i][j] = 0
                merged[i][mov + 1] = True
            elif mov != j:
                graph[i][mov] = graph[i][j]
                graph[i][j] = 0
    return graph


def dfs(depth, tmp_graph):
    global ans
    tmp = -sys.maxsize
    if depth == 5:
        for i in range(sz):
            tmp = max(tmp, max(tmp_graph[i]))
        ans = max(ans, tmp)
        return

    dfs(depth + 1, move_up(deepcopy(tmp_graph)))
    dfs(depth + 1, move_down(deepcopy(tmp_graph)))
    dfs(depth + 1, move_left(deepcopy(tmp_graph)))
    dfs(depth + 1, move_right(deepcopy(tmp_graph)))


dfs(0, rawdata)
print(ans)
