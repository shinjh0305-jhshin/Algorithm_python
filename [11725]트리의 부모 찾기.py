import sys
from collections import deque
Input = sys.stdin.readline
nodes = int(Input())
graph = [[] for _ in range(nodes + 1)]
parent = [-1 for _ in range(nodes + 1)]


def initialize():
    for _ in range(nodes - 1):
        m, n = map(int, Input().split())
        graph[m].append(n)
        graph[n].append(m)


def operate():
    initialize()

    qu = deque()
    qu.append(1)

    while qu:
        cn = qu.popleft()
        for nn in graph[cn]:
            if parent[nn] == -1:
                parent[nn] = cn
                qu.append(nn)

    print(*parent[2:], sep='\n')

operate()