import sys
Input = sys.stdin.readline


def find(node):
    if parent[node] < 0:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return

    if parent[root_a] > parent[root_b]:
        root_a, root_b = root_b, root_a
    parent[root_a] += parent[root_b]
    parent[root_b] = root_a


cities = int(Input())
plans = int(Input())
parent = [-1 for _ in range(cities + 1)]
for i in range(cities):
    tmp = list(map(int, Input().split()))
    for j in range(i + 1):
        if tmp[j]:
            union(i + 1, j + 1)
travelroute = list(map(int, Input().split()))
groupid = find(travelroute[0])
flag = True
for j in range(1, plans):
    if groupid != find(travelroute[j]):
        flag = False
        break
if not flag:
    print("NO")
else:
    print("YES")