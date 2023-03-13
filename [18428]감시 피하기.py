import sys
from collections import deque
from itertools import combinations
Input = sys.stdin.readline
sz = int(Input())
k = [list(Input().split()) for _ in range(sz)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
blank, teacher = [], []


def initialize():
    for i in range(sz):
        for j in range(sz):
            if k[i][j] == 'X':
                blank.append((i, j))
            elif k[i][j] == 'T':
                teacher.append((i, j))


def change(point, ch):
    for x, y in point:
        k[x][y] = ch


def find_student(o):
    change(o, 'O')

    for tx, ty in teacher:
        for i in range(4):
            cx, cy = tx, ty
            while True:
                cx, cy = cx + dx[i], cy + dy[i],
                if 0 <= cx < sz and 0 <= cy < sz:
                    if k[cx][cy] == 'S':
                        change(o, 'X')
                        return True
                    elif k[cx][cy] == 'O':
                        break
                else:
                    break

    change(o, 'X')
    return False


def operate():
    for tmp in combinations(blank, 3):
        if not find_student(tmp):
            print("YES")
            return
    print("NO")


initialize()
operate()

