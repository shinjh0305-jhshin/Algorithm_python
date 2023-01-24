import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
root = [-1] * (nodes + 1)
pq = []


def initialize():
    for _ in range(edges):
        a, b, c = map(int, Input().split())
        heappush(pq, (c, a, b))  # cost, start, end


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
    ans = 0
    used_edge = 0
    while used_edge != nodes - 1:
        c, s, e = heappop(pq)
        if union(s, e):
            ans += c
            used_edge += 1
    print(ans)


initialize()
operate()