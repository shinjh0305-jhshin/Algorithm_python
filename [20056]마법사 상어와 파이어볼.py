import sys
from collections import deque
Input = sys.stdin.readline
sz, balls, it = map(int, Input().split())
k = [[[] for _ in range(sz)] for _ in range(sz)]  # 질량, 방향, 속도
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
ball, mul_ball = deque(), deque()


def initialize():
    for _ in range(balls):
        r, c, m, s, d = map(int, Input().split())
        ball.append([r - 1, c - 1])
        k[r - 1][c - 1].append([m, d, s])


def move_balls():
    global k
    nk = [[[] for _ in range(sz)] for _ in range(sz)]  # 질량, 방향, 속도

    len_ball = len(ball)
    for _ in range(len_ball):
        i, j = ball.popleft()
        for cm, cd, cs in k[i][j]:
            ndx, ndy = dx[cd] * cs, dy[cd] * cs
            # 환산해준다
            tdx, tdy = abs(ndx) % sz, abs(ndy) % sz
            nx = (i + tdx) % sz if ndx >= 0 else (i - tdx) % sz
            ny = (j + tdy) % sz if ndy >= 0 else (j - tdy) % sz
            if len(nk[nx][ny]) == 1:
                mul_ball.append([nx, ny])
            elif not nk[nx][ny]:
                ball.append([nx, ny])
            nk[nx][ny].append([cm, cd, cs])
    k = nk


def split_balls():
    while mul_ball:
        i, j = mul_ball.popleft()
        sum_s, sum_m = 0, 0
        odd, even = False, False

        for cm, cd, cs in k[i][j]:
            sum_s += cs
            sum_m += cm
            if cd % 2:
                odd = True
            else:
                even = True

        new_s, new_m = sum_s // len(k[i][j]), sum_m // 5
        new_d = 1 if odd and even else 0
        k[i][j].clear()

        while new_m and new_d < 8:
            k[i][j].append([new_m, new_d, new_s])
            new_d += 2


def get_sum():
    ans = 0
    for i, j in ball:
        for x in k[i][j]:
            ans += x[0]
    print(ans)


def operate():
    for _ in range(it):
        move_balls()
        split_balls()
    get_sum()


initialize()
operate()
