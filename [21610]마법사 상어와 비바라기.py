import sys
from functools import reduce
Input = sys.stdin.readline
sz, it = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
mov = [list(map(int, Input().split())) for _ in range(it)]
cloud = {(sz - 2, 0), (sz - 2, 1), (sz - 1, 0), (sz - 1, 1)}  # 이전 단계에서 생성된 구름
dx, dy = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]


def move_cloud_and_rain(idx):
    global cloud

    # move cloud
    d, l = mov[idx]
    next_cloud = set()
    for cx, cy in cloud:
        tdx, tdy = abs((dx[d] * l)) % sz, abs((dy[d] * l)) % sz
        nx = (cx - tdx) % sz if dx[d] < 0 else (cx + tdx) % sz
        ny = (cy - tdy) % sz if dy[d] < 0 else (cy + tdy) % sz
        next_cloud.add((nx, ny))
    cloud = next_cloud

    # rained
    for i, j in next_cloud:
        k[i][j] += 1


def duplicate_rain():
    for cx, cy in cloud:
        for d in range(2, 9, 2):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < sz and 0 <= ny < sz and k[nx][ny]:
                k[cx][cy] += 1


def make_cloud():
    global cloud

    new_cloud = set()
    for i in range(sz):
        for j in range(sz):
            if k[i][j] >= 2 and (i, j) not in cloud:
                new_cloud.add((i, j))
                k[i][j] -= 2
    cloud = new_cloud


def operate():
    for i in range(it):
        move_cloud_and_rain(i)
        duplicate_rain()
        make_cloud()
    print(reduce(lambda acc, cur: acc + sum(cur), k, 0))


operate()
