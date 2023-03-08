import sys
Input = sys.stdin.readline
nodes, rels, money = map(int, Input().split())
k = [0] + list(map(int, Input().split()))
root = [-1] * (nodes + 1)
ans = [sys.maxsize] * (nodes + 1)


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

    if root_a > root_b:
        root_a, root_b = root_b, root_a

    root[root_a] += root[root_b]
    root[root_b] = root_a


def operate():
    for _ in range(rels):
        x, y = map(int, Input().split())
        union(x, y)
    for i in range(1, nodes + 1):
        root_i = find(i)
        ans[root_i] = min(ans[root_i], k[i])
    fee_sum = sum(list(filter(lambda x: x != sys.maxsize, ans)))

    if fee_sum <= money:
        print(fee_sum)
    else:
        print("Oh no")


operate()