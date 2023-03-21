import sys
Input = sys.stdin.readline
nodes, edges = map(int, Input().split())
forward, backward = [[] for _ in range(nodes + 1)], [[] for _ in range(nodes + 1)]
visited = [False] * (nodes + 1)
nodes_visited = 0


def initialize():
    for _ in range(edges):
        x, y = map(int, Input().split())
        forward[x].append(y)
        backward[y].append(x)


def dfs(k, cn):
    global nodes_visited
    visited[cn] = True
    for nn in k[cn]:
        if not visited[nn]:
            nodes_visited += 1
            dfs(k, nn)


def operate():
    ans = 0
    global visited, nodes_visited
    for i in range(1, nodes + 1):
        dfs(forward, i)
        visited = [False] * (nodes + 1)
        dfs(backward, i)
        visited = [False] * (nodes + 1)

        if nodes_visited == nodes - 1:
            ans += 1
        nodes_visited = 0
    print(ans)


initialize()
operate()