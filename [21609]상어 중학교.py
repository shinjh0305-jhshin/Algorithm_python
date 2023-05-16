import sys
from collections import deque

Input = sys.stdin.readline
sz, colors = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = []
result = 0


def group_block(i, j):
    cur_visited = {(i, j)}
    target_color = k[i][j]
    visited[i][j] = True
    qu = deque([(i, j)])
    blocks = 1
    rainbow_blocks = 0
    left_up_block = (i, j)

    while qu:
        cx, cy = qu.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < sz and 0 <= ny < sz:
                if k[nx][ny] < 0 or (k[nx][ny] > 0 and k[nx][ny] != target_color):  # 검은색 or 빈칸 or 다른색
                    continue
                if (nx, ny) in cur_visited:  # 방문한 적 있다
                    continue
                if k[nx][ny] == target_color:  # 같은 색
                    visited[nx][ny] = True
                    if (nx, ny) < left_up_block:
                        left_up_block = (nx, ny)
                elif k[nx][ny] == 0:  # 무지개 블록
                    rainbow_blocks += 1
                cur_visited.add((nx, ny))
                blocks += 1
                qu.append((nx, ny))
    return blocks, rainbow_blocks, left_up_block


def find_start():
    global visited, result
    visited = [[False] * sz for _ in range(sz)]
    max_blocks, max_rainbow_blocks, max_left_up_block = 0, 0, (0, 0)
    start = (0, 0)

    for i in range(sz):
        for j in range(sz):
            if k[i][j] > 0 and not visited[i][j]:
                blocks, rainbow_blocks, left_up_block = group_block(i, j)
                if blocks > max_blocks or (blocks == max_blocks and rainbow_blocks > max_rainbow_blocks) \
                        or (blocks == max_blocks and rainbow_blocks == max_rainbow_blocks and left_up_block > max_left_up_block):
                    max_blocks, max_rainbow_blocks, max_left_up_block = blocks, rainbow_blocks, left_up_block
                    start = (i, j)

    if max_blocks <= 1:
        return False

    result += max_blocks ** 2
    erase_block(start)
    gravitate()
    rotate_left()
    gravitate()

    return True


def erase_block(start):
    qu = deque([start])
    color = k[start[0]][start[1]]
    k[start[0]][start[1]] = -2

    while qu:
        cx, cy = qu.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < sz and 0 <= ny < sz and (k[nx][ny] == 0 or k[nx][ny] == color):
                k[nx][ny] = -2
                qu.append((nx, ny))


def gravitate():
    for col in range(sz):
        for row in range(sz - 1, 0, -1):
            if k[row][col] == -2:
                for ori_row in range(row - 1, -1, -1):
                    if k[ori_row][col] == -1:
                        break
                    if k[ori_row][col] >= 0:
                        k[row][col] = k[ori_row][col]
                        k[ori_row][col] = -2
                        break


def rotate_left():
    global k
    tk = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        for j in range(sz):
            tk[sz - j - 1][i] = k[i][j]
    k = tk


while True:
    res = find_start()
    if not res:
        print(result)
        break
