import sys
from collections import deque
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]
dp = [[0] * sz for _ in range(sz)]
qu = deque()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = [[False] * sz for _ in range(sz)]


def group_island(x, y, idx):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    k[x][y] = idx
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < sz and 0 <= ny < sz and not visited[nx][ny] and k[nx][ny]:
                visited[nx][ny] = True
                k[nx][ny] = idx
                q.append((nx, ny))


def initialize():
    idx = 1
    for i in range(sz):
        for j in range(sz):
            if k[i][j]:
                qu.append((i, j))
                if not visited[i][j]:
                    group_island(i, j, idx)
                    idx += 1


def operate():
    dist = 1
    ans = sys.maxsize
    flag = False
    while not flag:
        len_qu = len(qu)
        for _ in range(len_qu):
            cx, cy = qu.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < sz and 0 <= ny < sz and k[nx][ny] != k[cx][cy]:
                    if not dp[nx][ny]:
                        dp[nx][ny] = dist
                        k[nx][ny] = k[cx][cy]
                        qu.append((nx, ny))
                    else:
                        flag = True
                        ans = min(ans, dist + dp[nx][ny] - 1)
        dist += 1
    return ans


initialize()
print(operate())
