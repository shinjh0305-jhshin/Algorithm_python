from collections import deque
k = [list(input().rstrip()) for _ in range(12)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = []


def clear(x, y):
    qu, to_clear = deque(), deque()
    visited[x][y] = True

    qu.append([x, y])
    to_clear.append([x, y])
    ch = k[x][y]

    while qu:
        cx, cy = qu.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and k[nx][ny] == ch and not visited[nx][ny]:
                visited[nx][ny] = True
                qu.append([nx, ny])
                to_clear.append([nx, ny])

    if len(to_clear) >= 4:
        for x, y in to_clear:
            k[x][y] = '.'
        return True
    else:
        return False


def collapse():
    for j in range(6):
        for i in range(11, -1, -1):
            if k[i][j] != '.':
                ni = i
                while ni + 1 < 12 and k[ni + 1][j] == '.':
                    ni += 1
                k[ni][j] = k[i][j]
                if ni != i:
                    k[i][j] = '.'


def operate():
    ans = 0
    while True:
        global visited
        visited = [[False] * 6 for _ in range(12)]
        flag = False
        for i in range(12):
            for j in range(6):
                if k[i][j] != '.' and not visited[i][j] and clear(i, j):
                    flag = True
        if flag:
            ans += 1
            collapse()
        else:
            print(ans)
            return


operate()
