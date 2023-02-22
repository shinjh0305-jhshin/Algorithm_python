import sys
from itertools import permutations
from copy import deepcopy
Input = sys.stdin.readline
rows, cols, ops = map(int, Input().split())
graph = [list(map(int, Input().split())) for _ in range(rows)]
op = [tuple(map(int, Input().split())) for _ in range(ops)]


def rotate(r, c, s, k):
    for i in range(1, s + 1):
        tmp = k[r - i][c - i]
        # k[r - i + 1][c - i] ~ k[r + i][c - i] 1 row up
        for j in range(r - i + 1, r + i + 1):
            k[j - 1][c - i] = k[j][c - i]
        # k[r + i][c - i + 1] ~ k[r + i][c + i] 1 col left
        for j in range(c - i + 1, c + i + 1):
            k[r + i][j - 1] = k[r + i][j]
        # k[r + i - 1][c + i] ~ k[r - i][c + i] 1 row down
        for j in range(r + i - 1, r - i - 1, -1):
            k[j + 1][c + i] = k[j][c + i]
        # k[r - i][c + i - 1] ~ k[r - i][c - i + 1] 1 col right
        for j in range(c + i - 1, c - i, -1):
            k[r - i][j + 1] = k[r - i][j]
        k[r - i][c - i + 1] = tmp


def make_min(order):
    tmp = deepcopy(graph)
    for i in order:
        rotate(op[i][0] - 1, op[i][1] - 1, op[i][2], tmp)
    ans = sys.maxsize
    for i in range(rows):
        ans = min(ans, sum(tmp[i]))
    return ans


def operate():
    ans = sys.maxsize
    for order in permutations(range(ops)):
        ans = min(ans, make_min(order))
    print(ans)


operate()
