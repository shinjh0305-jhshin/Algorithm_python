import sys
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
root = [-1] * (nodes + 1)


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

    if root[root_a] > root[root_b]:
        root_a, root_b = root_b, root_a

    root[root_a] += root[root_b]
    root[root_b] = root_a
    return True


def operate():
    ans = 1
    for _ in range(edges):
        x, y = map(int, Input().split())
        if not union(x, y):
            print(ans)
            return
        ans += 1
    print(0)


operate()



