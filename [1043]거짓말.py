import sys
Input = sys.stdin.readline


def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return

    if parent[root_a] > parent[root_b]:
        root_a, root_b = root_b, root_a
    parent[root_a] += parent[root_b]
    parent[root_b] = root_a


peoples, parties = map(int, Input().split())
# People who knows truth
tmp = list(map(int, Input().split()))
if tmp[0] == 0:
    print(parties)
else:
    parent = [-1 for _ in range(peoples + 1)]
    for i in range(2, tmp[0] + 1):
        union(tmp[1], tmp[i])

    party = [[] for _ in range(parties)]

    for i in range(parties):
        party[i] = list(map(int, Input().split()))
        for j in range(2, party[i][0] + 1):
            union(party[i][1], party[i][j])

    truthRoot = find(tmp[1])
    ans = 0

    for i in range(parties):
        flag = True
        for j in range(1, party[i][0] + 1):
            if find(party[i][j]) == truthRoot:
                flag = False
                break
        if flag:
            ans += 1

    print(ans)