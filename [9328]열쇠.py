import sys
from collections import defaultdict, deque
Input = sys.stdin.readline
tc = int(Input())
rows, cols = 0, 0
k, visited = [], []
key_found = set()
door = defaultdict(list)  # lower(key) : pos
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    global rows, cols, k, visited
    rows, cols = map(int, Input().split())
    k = [['.'] * (cols + 2)] + [['.'] + list(Input().rstrip()) + ['.'] for _ in range(rows)] + [['.'] * (cols + 2)]
    rows, cols = rows + 2, cols + 2
    key_found.clear()
    key_found.update(list(Input().rstrip()))

    door.clear()
    for i in range(rows):
        for j in range(cols):
            if k[i][j].isupper():
                door[k[i][j].lower()].append([i, j])

    for key in list(key_found):
        for x, y in door[key]:
            k[x][y] = '.'  # 최초의 갖고 있는 열쇠로 열 수 있는 문은 열어둔다

    visited = [[False] * cols for _ in range(rows)]


def operate():
    global visited
    qu = deque([[0, 0]])
    visited[0][0] = True
    ans = 0
    while qu:
        x, y = qu.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                if k[nx][ny].isupper() or k[nx][ny] == '*':  # 안 열린 문이거나 벽이다
                    continue
                elif k[nx][ny].islower():  # 열쇠다
                    if k[nx][ny] not in key_found:  # 처음 발견한 종류의 열쇠면 문을 열어놓는다
                        key_found.add(k[nx][ny])
                        visited = [[False] * cols for _ in range(rows)]
                        for door_x, door_y in door[k[nx][ny]]:
                            k[door_x][door_y] = '.'
                elif k[nx][ny] == '$':  # 문서다
                    k[nx][ny] = '.'  # visited가 중간에 초기화되므로 아예 제거 필요
                    ans += 1
                visited[nx][ny] = True
                qu.append([nx, ny])
    print(ans)


for _ in range(tc):
    initialize()
    operate()
