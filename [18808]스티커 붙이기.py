import sys
from collections import deque
Input = sys.stdin.readline
rows, cols, stickers = map(int, Input().split())
sz_sticker = []
sticker = [[] for _ in range(stickers)]
board = [[0] * cols for _ in range(rows)]


def initialize():
    for idx in range(stickers):
        r, c = map(int, Input().split())
        sz_sticker.append([r, c])
        cur_sticker = [list(map(int, Input().split())) for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if cur_sticker[i][j]:
                    sticker[idx].append([i, j])


def rotate(idx):
    cr, cc = sz_sticker[idx]
    for i in range(len(sticker[idx])):
        cx, cy = sticker[idx][i]
        sticker[idx][i] = [cy, cr - cx - 1]
    sz_sticker[idx] = [cc, cr]


def is_stickable(sx, sy, idx):
    for dx, dy in sticker[idx]:
        cx, cy = sx + dx, sy + dy
        if board[cx][cy]:
            return False
    return True


def mark_board(sx, sy, idx):
    for dx, dy in sticker[idx]:
        cx, cy = sx + dx, sy + dy
        board[cx][cy] = 1


def stick(idx):
    for _ in range(4):  # rotate
        sr, sc = sz_sticker[idx]
        for sx in range(rows - sr + 1):
            for sy in range(cols - sc + 1):
                if is_stickable(sx, sy, idx):
                    mark_board(sx, sy, idx)
                    return
        rotate(idx)


def operate():
    for idx in range(stickers):
        stick(idx)
    ans = 0
    for i in range(rows):
        ans += board[i].count(1)
    print(ans)


initialize()
operate()
