import sys
from collections import deque
Input = sys.stdin.readline
sz, horses = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
horse_info = []  # row, col, dir
horse_stack = [[deque() for _ in range(sz)] for _ in range(sz)]  # index
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]


def initialize():
    for i in range(horses):
        x, y, d = map(int, Input().split())
        x, y, d = x - 1, y - 1, d - 1
        horse_info.append([x, y, d])
        horse_stack[x][y].append(i)


def operate():
    turn = 1
    tmp_qu = deque()
    while True:
        if turn > 1000:
            print(-1)
            return
        for h in range(horses):
            cx, cy, cd = horse_info[h]
            nx, ny = cx + dx[cd], cy + dy[cd]
            if not (0 <= nx < sz and 0 <= ny < sz) or k[nx][ny] == 2:  # 칸을 벗어나는 경우 or 파란색인 경우
                cd = cd - 1 if cd % 2 else cd + 1
                nx, ny = cx + dx[cd], cy + dy[cd]
                horse_info[h] = [cx, cy, cd]
                if not (0 <= nx < sz and 0 <= ny < sz) or k[nx][ny] == 2:
                    continue
            while True:
                cur_horse = horse_stack[cx][cy].pop()
                horse_info[cur_horse][0], horse_info[cur_horse][1] = nx, ny
                if k[nx][ny] == 0:
                    tmp_qu.appendleft(cur_horse)
                else:
                    horse_stack[nx][ny].append(cur_horse)
                if cur_horse == h:
                    break
            if k[nx][ny] == 0:
                horse_stack[nx][ny].extend(tmp_qu)
                tmp_qu.clear()
            if len(horse_stack[nx][ny]) >= 4:
                print(turn)
                return
        turn += 1


initialize()
operate()
