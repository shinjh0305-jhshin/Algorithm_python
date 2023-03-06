import sys
sys.setrecursionlimit(10 ** 6)
k = [[] for _ in range(6)]
op = list(map(int, input().split()))
h = [(0, 0) for _ in range(4)]
occupied = [[False] * 30 for _ in range(6)]
ans = 0


def initialize():
    for i in range(0, 41, 2):
        k[0].append(i)
    k[1] += [10, 13, 16, 19, 25]
    k[2] += [20, 22, 24, 25]
    k[3] += [30, 28, 27, 26, 25]
    k[4] += [25, 30, 35, 40]
    k[5] += [40]


def move_horse(r, c, cnt):
    for _ in range(cnt):
        if c == len(k[r]) - 1:
            if 1 <= r <= 3:
                r, c = 4, 1
            elif r == 0 or r >= 4:  # 종료
                return 0, -1, -1  # 점수, row, col
        else:
            c += 1
    if r == 0:
        if k[r][c] == 10:
            r, c = 1, 0
        elif k[r][c] == 20:
            r, c = 2, 0
        elif k[r][c] == 30:
            r, c = 3, 0
        elif k[r][c] == 40:
            r, c = 5, 0
    elif k[r][c] == 25:
        r, c = 4, 0
    elif k[r][c] == 40:
        r, c = 5, 0
    return k[r][c], r, c


def dfs(idx=0, cur_sum=0):
    if idx == 10:
        global ans
        ans = max(ans, cur_sum)
        return
    for i in range(4):
        if h[i] == (-1, -1):
            continue
        ch = h[i]
        tmp = move_horse(ch[0], ch[1], op[idx])

        if tmp[1] == -1:
            h[i] = (-1, -1)
        else:
            if occupied[tmp[1]][tmp[2]]:
                continue
            h[i] = (tmp[1], tmp[2])
            occupied[tmp[1]][tmp[2]] = True  # 앞으로 갈 위치 occupied

        occupied[ch[0]][ch[1]] = False  # 기존에 있었던 위치 unoccupy
        dfs(idx + 1, cur_sum + tmp[0])
        occupied[ch[0]][ch[1]] = True  # 기존에 있었던 위치 occupy

        if tmp[1] != -1:
            occupied[tmp[1]][tmp[2]] = False

        h[i] = ch


def operate():
    dfs()
    print(ans)


initialize()
operate()
