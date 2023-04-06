import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
sz = int(Input())
k = [[0, 0] for _ in range(sz + 1)]
tree_sz = [0] * (sz + 1)
root = 0


def initialize():
    global k
    for _ in range(sz):
        n, x, y = map(int, Input().split())
        x = 0 if x == -1 else x
        y = 0 if y == -1 else y
        k[n] = [x, y]


def find_root():
    global root
    visited = [False] * (sz + 1)
    for i, j in k:
        visited[i] = visited[j] = True
    root = visited.index(False)


def get_size(idx):
    if idx == 0:
        return 0
    tree_sz[idx] = get_size(k[idx][0]) + get_size(k[idx][1]) + 1
    return tree_sz[idx]


def find_width():
    qu = deque()
    qu.append([root, 0, 'R'])
    pos = [0] * (sz + 1)
    ans_h, ans_w = 1, 1

    h = 1
    while qu:
        len_qu = len(qu)
        left, right = 0, 0

        for i in range(len_qu):
            idx, prev_pos, lr = qu.popleft()

            if lr == 'L':
                pos[idx] = prev_pos - tree_sz[k[idx][1]] - 1
            elif lr == 'R':
                pos[idx] = prev_pos + tree_sz[k[idx][0]] + 1

            if i == 0:
                left = pos[idx]
            elif i == len_qu - 1:
                right = pos[idx]

            if k[idx][0]:
                qu.append([k[idx][0], pos[idx], 'L'])
            if k[idx][1]:
                qu.append([k[idx][1], pos[idx], 'R'])

        if right - left + 1 > ans_w:
            ans_w = right - left + 1
            ans_h = h
        h += 1
    print(ans_h, ans_w)


initialize()
find_root()
get_size(root)
find_width()
