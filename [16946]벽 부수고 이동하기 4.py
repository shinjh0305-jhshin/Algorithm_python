import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [list(map(int, Input().rstrip())) for _ in range(rows)]
idx = [[0] * cols for _ in range(rows)]
cnt = {}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def dfs(cx, cy, cidx):
    idx[cx][cy] = cidx
    ans = 1
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < rows and 0 <= ny < cols:
            if k[nx][ny] == 0 and idx[nx][ny] == 0:
                ans += dfs(nx, ny, cidx)
    return ans


def operate():
    cidx = 1
    for i in range(rows):
        for j in range(cols):
            if k[i][j] == 0 and idx[i][j] == 0:
                ret = dfs(i, j, cidx)
                cnt[cidx] = ret
                cidx += 1

    tmp = set()
    ans = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if k[i][j] == 1:
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < rows and 0 <= ny < cols and k[nx][ny] == 0:
                        cidx = idx[nx][ny]
                        if cidx not in tmp:
                            ans[i][j] += cnt[cidx]
                            tmp.add(cidx)
                ans[i][j] += 1
                ans[i][j] %= 10
                tmp.clear()
    for i in range(rows):
        print(*ans[i], sep='')


operate()
