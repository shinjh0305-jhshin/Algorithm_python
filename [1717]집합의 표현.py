import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline


def find(x):
    if root[x] < 0:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if root[root_x] > root[root_y]:
        root_x, root_y = root_y, root_x

    root[root_x] += root[root_y]
    root[root_y] = root_x


def same(x, y):
    if find(x) == find(y):
        print("YES")
    else:
        print("NO")


nodes, operations = map(int, Input().split())
root = [-1 for _ in range(nodes + 1)]
for _ in range(operations):
    mode, a, b = map(int, Input().split())
    if mode == 0:  # Union
        union(a, b)
    else:  # Find
        same(a, b)