import sys
Input = sys.stdin.readline
tc = int(Input())
root = []


def find(a):
    if root[a] < 0:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return -root[root_a]
    if root[root_a] > root[root_b]:
        root_a, root_b = root_b, root_a
    root[root_a] += root[root_b]
    root[root_b] = root_a
    return -root[root_a]


def operate():
    sz = int(Input())
    friends = []
    ans = []
    dat = {}
    for _ in range(sz):
        k = list(Input().split())
        k_idx = [0, 0]
        for i in range(2):
            try:
                k_idx[i] = dat[k[i]]
            except KeyError:
                dat[k[i]] = len(dat)
                k_idx[i] = len(dat) - 1
        friends.append(k_idx)

    global root
    root = [-1] * len(dat)
    for k_idx in friends:
        ans.append(union(k_idx[0], k_idx[1]))
    print(*ans, sep='\n')


for _ in range(tc):
    operate()
