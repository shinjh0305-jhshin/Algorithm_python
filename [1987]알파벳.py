import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [Input().rstrip() for _ in range(rows)]
visited = [False] * 26
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
ans = 0


def dfs(cx=0, cy=0, depth=1):
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < rows and 0 <= ny < cols and not visited[ord(k[nx][ny]) - ord('A')]:
            visited[ord(k[nx][ny]) - ord('A')] = True
            dfs(nx, ny, depth + 1)
            visited[ord(k[nx][ny]) - ord('A')] = False
    global ans
    ans = max(ans, depth)


def operate():
    visited[ord(k[0][0]) - ord('A')] = True
    dfs()
    print(ans)


operate()