import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [Input().rstrip() for _ in range(rows)]
root = [-1] * (rows * cols)
d_idx = {'D': 0, 'L': 1, 'U': 2, 'R': 3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def find(a):
    if root[a] < 0:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False

    if root_a > root_b:
        root_a, root_b = root_b, root_a

    root[root_a] += root[root_b]
    root[root_b] = root_a
    return True


def search(cx, cy):
    while True:
        d = d_idx[k[cx][cy]]
        nx, ny = cx + dx[d], cy + dy[d]
        if not union(cx * cols + cy, nx * cols + ny):
            break
        cx, cy = nx, ny


def operate():
    for i in range(rows):
        for j in range(cols):
            if root[i * cols + j] == -1:
                search(i, j)
    ans = 0
    for x in root:
        if x < 0:
            ans += 1
    print(ans)

operate()