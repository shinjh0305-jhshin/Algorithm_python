import sys
from itertools import combinations
Input = sys.stdin.readline
cols, sz, rows = map(int, Input().split())
bridge = [[False] * (cols + 1) for _ in range(rows + 1)]
no_bridge = []  # 연결선이 없는 곳


def initialize():
    for _ in range(sz):
        r, c = map(int, Input().split())
        bridge[r][c] = True
    for i in range(1, rows + 1):
        for j in range(1, cols):
            if not bridge[i][j] and not (bridge[i][j - 1] or bridge[i][j + 1]):
                no_bridge.append([i, j])


def check_bridge(tmp_bridge):
    for k in range(0, len(tmp_bridge) - 1):
        if tmp_bridge[k][0] == tmp_bridge[k + 1][0] and tmp_bridge[k][1] + 1 == tmp_bridge[k + 1][1]:
            return False
    return True


def make_clear_bridge(dat):
    for r, c in dat:
        bridge[r][c] = not bridge[r][c]


def play():
    for c in range(1, cols + 1):
        cur_col = c
        for r in range(1, rows + 1):
            if bridge[r][cur_col - 1]:
                cur_col -= 1
            elif bridge[r][cur_col]:
                cur_col += 1
        if cur_col != c:
            return False
    return True


def operate():
    for i in range(0, 4):
        for tmp_bridge in combinations(no_bridge, i):
            if not check_bridge(tmp_bridge):
                continue
            make_clear_bridge(tmp_bridge)
            if play():
                print(i)
                return
            make_clear_bridge(tmp_bridge)
    print(-1)


initialize()
operate()
