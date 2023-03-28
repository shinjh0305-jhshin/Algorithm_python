import sys
from collections import deque
from functools import reduce
Input = sys.stdin.readline
plates, nums, rotas = map(int, Input().split())
plate = [deque(list(map(int, Input().split()))) for _ in range(plates)]
rota = [list(map(int, Input().split())) for _ in range(rotas)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def rotate(idx):
    if rota[idx][1] == 0:  # 시계방향
        mov = rota[idx][2]
    else:  # 반시계방향
        mov = -rota[idx][2]

    plate_idx = rota[idx][0] - 1
    while plate_idx < plates:
        plate[plate_idx].rotate(mov)
        plate_idx += rota[idx][0]


def erase_num():
    flag = False
    qu = deque()
    for x in range(plates):
        for y in range(nums):
            if plate[x][y] > 0:  # 방문한 적이 없다
                qu.append([x, y])
                cur_num = plate[x][y]
                while qu:
                    cx, cy = qu.popleft()
                    for i in range(4):
                        nx, ny = cx + dx[i], (cy + dy[i]) % nums
                        if nx < 0 or nx >= plates:
                            continue
                        if cur_num == plate[nx][ny]:
                            flag = True
                            plate[cx][cy] = plate[nx][ny] = 0
                            qu.append([nx, ny])
    return flag


def modify_num():
    tmp_num = []
    for i in range(plates):
        tmp_num.extend(list(filter(lambda x: x > 0, plate[i])))
    if len(tmp_num) == 0:
        return
    avg = sum(tmp_num) / len(tmp_num)

    for i in range(plates):
        for j in range(nums):
            if plate[i][j]:
                if plate[i][j] > avg:
                    plate[i][j] -= 1
                elif plate[i][j] < avg:
                    plate[i][j] += 1


def operate():
    for i in range(rotas):
        rotate(i)
        res = erase_num()
        if not res:
            modify_num()
    print(reduce(lambda acc, cur: acc + sum(cur), plate, 0))


operate()