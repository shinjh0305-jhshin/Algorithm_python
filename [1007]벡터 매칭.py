import sys
from math import sqrt
from itertools import combinations
Input = sys.stdin.readline
tc = int(Input())
sz = 0
k = []


def vector_sum(start):
    mov = 0
    sx, sy, ex, ey = 0, 0, 0, 0
    for i in range(sz):
        if mov < sz // 2 and i == start[mov]:
            sx += k[i][0]
            sy += k[i][1]
            mov += 1
        else:
            ex += k[i][0]
            ey += k[i][1]
    return sqrt(pow(ex - sx, 2) + pow(ey - sy, 2))


def operate():
    global sz, k
    sz = int(Input())
    k = [tuple(map(int, Input().split())) for _ in range(sz)]
    ans = sys.maxsize
    for start in combinations(range(sz), sz // 2):  # 벡터의 절반을 시작점으로 잡는다
        ans = min(ans, vector_sum(start))
    print(ans)


for _ in range(tc):
    operate()