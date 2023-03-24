import sys
from collections import deque
Input = sys.stdin.readline
stories, rows, cols, graph = 0, 0, 0, []
s, e, visited = [], [], []
ds, dx, dy = [1, -1], [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    global stories, rows, cols, graph, s, e, visited
    stories, rows, cols = map(int, Input().split())
    if stories == 0:
        return False

    graph = []
    for i in range(stories):
        graph.append([list(Input().rstrip()) for _ in range(rows)])
        Input()

    visited = [[[False] * cols for _ in range(rows)] for _ in range(stories)]

    found_s, found_e = False, False
    for k in range(stories):
        for i in range(rows):
            for j in range(cols):
                if graph[k][i][j] == 'S':
                    s = [k, i, j]
                    found_s = True
                    if found_e:
                        return True
                elif graph[k][i][j] == 'E':
                    e = [k, i, j]
                    graph[k][i][j] = '.'
                    found_e = True
                    if found_s:
                        return True


def operate():
    qu = deque([s])
    t = 0
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cs, cx, cy = qu.popleft()
            if e == [cs, cx, cy]:
                return f'Escaped in {t} minute(s).'
            for k in ds:
                ns = cs + k
                if 0 <= ns < stories and graph[ns][cx][cy] == '.' and not visited[ns][cx][cy]:
                    visited[ns][cx][cy] = True
                    qu.append([ns, cx, cy])
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and graph[cs][nx][ny] == '.' and not visited[cs][nx][ny]:
                    visited[cs][nx][ny] = True
                    qu.append([cs, nx, ny])
        t += 1
    return 'Trapped!'


ans = []
while initialize():
    ans.append(operate())
print(*ans, sep='\n')

