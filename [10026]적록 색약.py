import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
sz = int(Input())
graph = [Input().rstrip() for _ in range(sz)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = [[False] * sz for _ in range(sz)]


def dfs(cx, cy, odd):
    visited[cx][cy] = True
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < sz and 0 <= ny < sz and not visited[nx][ny]:
            if graph[cx][cy] == graph[nx][ny]:
                dfs(nx, ny, odd)
            elif odd:
                if (graph[cx][cy] == 'R' and graph[nx][ny] == 'G') or (graph[cx][cy] == 'G' and graph[nx][ny] == 'R'):
                    dfs(nx, ny, odd)


def traverse(odd):
    ans = 0
    for i in range(sz):
        for j in range(sz):
            if not visited[i][j]:
                dfs(i, j, odd)
                ans += 1
    return ans


def operate():
    global visited
    ans = [traverse(False)]
    visited = [[False] * sz for _ in range(sz)]
    ans.append(traverse(True))
    print(*ans)


operate()