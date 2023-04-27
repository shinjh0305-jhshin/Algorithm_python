import sys
from collections import defaultdict
Input = sys.stdin.readline
sz, sharks, duration = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]  # 각 칸의 냄새 소유자
cur_pos = defaultdict(list)  # 각 상어의 위치
cur_dir = [0] + list(map(int, Input().split()))  # 각 상어의 방향
pri = [[list(map(int, Input().split())) for _ in range(4)] for _ in range(sharks)]  # 각 상어의 방향별 우선순위
odor_expires = defaultdict(list)  # 냄새가 사라지는 시각 : 좌표
odor_cnt = [[0] * sz for _ in range(sz)]  # 각 칸의 냄새의 mutex lock
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]


def initialize():
    global cur_pos
    for i in range(sz):
        for j in range(sz):
            if k[i][j]:
                cur_pos[k[i][j]] = [i, j]
                odor_expires[duration].append([i, j])
                odor_cnt[i][j] += 1
    cur_pos = dict(sorted(cur_pos.items()))


def remove_odor(t):
    for i, j in odor_expires[t]:
        if odor_cnt[i][j] == 1:
            k[i][j] = 0
        odor_cnt[i][j] -= 1
    del odor_expires[t]


def move_shark(t):
    global k
    blank, mine = [], []
    occupied = [[False] * sz for _ in range(sz)]
    nd = 0
    tk = [x[:] for x in k]
    to_del = []
    for i, c in cur_pos.items():
        cx, cy = c
        cd = cur_dir[i]
        blank.clear()
        mine.clear()
        for d in pri[i - 1][cd - 1]:
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < sz and 0 <= ny < sz:
                if k[nx][ny] == 0:  # 빈 칸을 발견함. 무조건 loop 탈출.
                    blank = [nx, ny]
                    nd = d
                    break
                elif k[nx][ny] == i and not mine:  # 내 냄새와 동일한 칸 처음 발견함.
                    mine = [nx, ny]
                    nd = d
        nx, ny = blank if blank else mine
        if occupied[nx][ny]:  # 더 낮은 상어가 먼저 와있음
            to_del.append(i)
            continue
        tk[nx][ny] = i
        cur_pos[i] = [nx, ny]
        cur_dir[i] = nd
        odor_expires[t + duration].append([nx, ny])
        odor_cnt[nx][ny] += 1
        occupied[nx][ny] = True
    for x in to_del:
        del cur_pos[x]
    k = tk


def operate():
    t = 1
    while True:
        if t > 1000:
            print(-1)
            return
        move_shark(t)
        remove_odor(t)
        if len(cur_pos) == 1:
            print(t)
            return
        t += 1


initialize()
operate()
