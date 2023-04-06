import sys
from math import sqrt

Input = sys.stdin.readline
tc = int(Input())
nodes = 0
k, root = [], []


def initialize():
    global nodes, k, root
    nodes = int(Input())
    k = [list(map(int, Input().split())) for _ in range(nodes)]
    root = [-1] * nodes


def find(a):
    if root[a] < 0:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return

    if root[root_a] > root[root_b]:
        root_a, root_b = root_b, root_a

    root[root_a] += root[root_b]
    root[root_b] = root_a


def operate():
    for i in range(nodes):
        ix, iy, ir = k[i]
        for j in range(i + 1, nodes):
            jx, jy, jr = k[j]

            r = ir + jr
            d = sqrt(pow((ix - jx), 2) + pow((iy - jy), 2))

            if d <= r:
                union(i, j)

    print(len(list(filter(lambda x: root[x] < 0, range(nodes)))))


for _ in range(tc):
    initialize()
    operate()
