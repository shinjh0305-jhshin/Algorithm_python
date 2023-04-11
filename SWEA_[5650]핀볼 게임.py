tc = int(input())
k, wormhole, point, visited = [], [], [], []  # point : 블럭의 각 진입 방향에 따른 획득 가능 점수
sz = 0
res = 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
chg = [[0, 0, 0, 0], [3, 0, 1, 2], [2, 3, 1, 0], [1, 2, 3, 0], [3, 2, 0, 1], [3, 2, 1, 0]]  # 들어온 방향에 따른 나가는 방향


def initialize():
    global sz, k, wormhole, point, res
    sz = int(input())
    k = [list(map(int, input().split())) for _ in range(sz)]

    wormhole = [[] for _ in range(11)]
    for i in range(sz):
        for j in range(sz):
            if k[i][j] >= 6:
                wormhole[k[i][j]].append([i, j])

    point = [[[-1] * 4 for _ in range(sz)] for _ in range(sz)]
    res = 0


def get_point(i, j):
    block_t = k[i][j]
    print(">> Idx : ", i, j)
    for cd in range(4):  # 진입 방향
        print(">> cd : ", cd)
        d = chg[block_t][cd]  # 진출 방향
        if cd + d == 3:  # 진입방향 정 반대로 진출함
            point[i][j][cd] = 1
            continue
        cx, cy = i, j
        while True:
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < sz and 0 <= ny < sz:
                if k[nx][ny] == -1:  # 블랙홀
                    point[i][j][cd] = 1
                    break
                if k[nx][ny] == 0:  # 빈칸
                    cx, cy = nx, ny
                    continue
                if k[nx][ny] <= 5:  # 일반적인 블록
                    if point[nx][ny][d] == -1:  # 방문한적 없다
                        get_point(nx, ny)
                    point[i][j][cd] = point[nx][ny][d] + 2  # 점수 계산
                    break
                elif k[nx][ny] <= 10:  # 웜홀
                    hole_idx = k[nx][ny]
                    cx, cy = wormhole[hole_idx][0] if [nx, ny] == wormhole[hole_idx][1] else wormhole[hole_idx][1]
                    continue
            else:  # 가장자리
                point[i][j][cd] = 3
                break


def dfs(i, j, d):
    global res
    visited[i][j][d] = True
    nx, ny = i + dx[d], j + dy[d]
    if not (0 <= nx < sz and 0 <= ny < sz):
        res = max(res, 1)
    elif k[nx][ny] == -1:
        return
    elif k[nx][ny] == 0:
        if not visited[nx][ny][d]:
            dfs(nx, ny, d)
    elif k[nx][ny] <= 5:
        res = max(res, point[nx][ny][d])
    elif k[nx][ny] <= 10:
        hole_idx = k[nx][ny]
        cx, cy = wormhole[hole_idx][0] if [nx, ny] == wormhole[hole_idx][1] else wormhole[hole_idx][1]
        dfs(cx, cy, d)


def operate():
    for i in range(sz):
        for j in range(sz):
            if 1 <= k[i][j] <= 5 and point[i][j][0] == -1:  # 방문하지 않은 블록
                get_point(i, j)

    global visited
    visited = [[[False] * 4 for _ in range(sz)] for _ in range(sz)]
    for i in range(sz):
        for j in range(sz):
            if k[i][j] == 0:
                for d in range(4):
                    if not visited[i][j][d]:
                        dfs(i, j, d)
    print(res)


for _ in range(tc):
    initialize()
    operate()
