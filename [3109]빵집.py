import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline

rows, cols = map(int, Input().split())
graph = [Input().rstrip() for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
ans = 0


def dfs(cx, cy):
    if cy == cols - 1:
        global ans
        ans += 1
        return True
    for dx in range(-1, 2):
        nx = cx + dx
        ny = cy + 1
        if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False


def operate():
    for i in range(rows):
        dfs(i, 0)
    print(ans)


operate()