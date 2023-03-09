import sys
Input = sys.stdin.readline
nodes, edges = 0, 0
k, visited = [], []
p = []


def initialize():
    global k, nodes, edges, visited
    nodes, edges = map(int, Input().split())
    if nodes == 0:
        return False
    k = [[] for _ in range(nodes + 1)]
    visited = [False] * (nodes + 1)
    for _ in range(edges):
        x, y = map(int, Input().split())
        k[x].append(y)
        k[y].append(x)
    return True


def search(node, prev_node):
    visited[node] = True
    for nn in k[node]:
        if visited[nn] and nn != prev_node:
            return False
        if not visited[nn]:
            if not search(nn, node):
                return False
    return True


def operate():
    ans = 0
    if initialize():
        for i in range(1, nodes + 1):
            if not visited[i] and search(i, 0):
                ans += 1
        if ans > 1:
            p.append(f'Case {len(p) + 1}: A forest of {ans} trees.')
        elif ans == 1:
            p.append(f'Case {len(p) + 1}: There is one tree.')
        else:
            p.append(f'Case {len(p) + 1}: No trees.')
    else:
        return False
    return True


while operate():
    pass
print(*p, sep='\n')

