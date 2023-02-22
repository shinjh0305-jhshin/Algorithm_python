import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
x, y, d = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
to_clean = [0, 0, 0]


def not_cleaned(cx, cy, cd):
    for i in range(4):
        cd = (cd - 1) % 4
        nx, ny = cx + dx[cd], cy + dy[cd]
        if not visited[nx][ny] and k[nx][ny] == 0:
            global to_clean
            to_clean = [nx, ny, cd]
            return True
    return False


def operate():
    ans = 0
    cx, cy, cd = x, y, d
    while True:
        if not visited[cx][cy]:
            ans += 1
        visited[cx][cy] = True

        if not_cleaned(cx, cy, cd):
            cx, cy, cd = to_clean
        else:
            back_d = (cd + 2) % 4
            nx, ny = cx + dx[back_d], cy + dy[back_d]
            if 0 <= nx < rows and 0 <= ny < cols:
                if k[nx][ny] == 1:
                    break
                else:
                    cx, cy = nx, ny

    print(ans)


operate()
