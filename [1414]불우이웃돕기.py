import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
cpus = int(Input())
pq = []
root = [-1] * cpus


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


def operate():
    total_length = 0
    for i in range(cpus):
        tmp = Input().rstrip()
        for j in range(len(tmp)):
            if tmp[j] == '0':
                continue
            if 'a' <= tmp[j] <= 'z':
                ch_len = ord(tmp[j]) - ord('a') + 1
            else:
                ch_len = ord(tmp[j]) - ord('A') + 27
            total_length += ch_len
            heappush(pq, (ch_len, i, j))

    lans = 0
    while lans != cpus - 1:
        if not pq:
            print(-1)
            return
        c, i, j = heappop(pq)
        if union(i, j):
            total_length -= c
            lans += 1
    print(total_length)


operate()