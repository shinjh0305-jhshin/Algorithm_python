import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
graph = [list(Input().rstrip()) for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
rx, ry, bx, by = 0, 0, 0, 0
visited = [[[[False] * 10 for _ in range(10)] for _2 in range(10)] for _3 in range(10)]
ans = sys.maxsize


def initialize():
    global rx, ry, bx, by
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j


def tilt(d, k):
    global rx, ry, bx, by
    target = [(rx, ry), (bx, by)]
    if (d == 0 and rx < bx) or (d == 1 and ry > by) or (d == 2 and rx > bx) or (d == 3 and ry < by):
        target[0], target[1] = target[1], target[0]

    res = {}
    for i in range(2):
        cx, cy = target[i][0], target[i][1]
        ch = k[cx][cy]
        while True:
            nx, ny = cx + dx[d], cy + dy[d]
            if k[nx][ny] == 'O':
                k[target[i][0]][target[i][1]] = '.'
                res[ch] = True
                break
            elif k[nx][ny] != '.':
                k[target[i][0]][target[i][1]] = '.'
                k[cx][cy] = ch
                res[ch] = False

                if ch == 'R':
                    rx, ry = cx, cy
                else:
                    bx, by = cx, cy
                break
            cx, cy = nx, ny
    return res


def dfs(depth, k):
    global rx, ry, bx, by, ans

    if depth == 11 or depth >= ans or visited[rx][ry][bx][by]:
        return
    visited[rx][ry][bx][by] = True
    _rx, _ry, _bx, _by = rx, ry, bx, by

    for i in range(4):
        cp = [a[:] for a in k]
        res = tilt(i, cp)
        if res['B']:
            continue
        if res['R']:
            ans = min(ans, depth)
            return
        dfs(depth + 1, cp)
        rx, ry, bx, by = _rx, _ry, _bx, _by


def operate():
    dfs(1, graph)
    print(-1) if ans == sys.maxsize else print(ans)


initialize()
operate()
