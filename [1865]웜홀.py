import sys
Input = sys.stdin.readline
tc = int(Input())
nodes, edges, holes = 0, 0, 0
edge = []
INF = 2134567890


def initialize():
    global nodes, edges, holes
    nodes, edges, holes = map(int, Input().split())
    k = [[] for _ in range(nodes + 1)]
    edge.clear()
    for _ in range(edges):
        s, e, t = map(int, Input().split())
        edge.append([s, e, t])
        edge.append([e, s, t])
    for _ in range(holes):
        s, e, t = map(int, Input().split())
        edge.append([s, e, -t])


def operate():
    visited = [INF] * (nodes + 1)
    visited[1] = 0
    for v in range(nodes):
        for s, e, t in edge:
            if visited[s] + t < visited[e]:
                if v == nodes - 1:
                    return True
                visited[e] = visited[s] + t
    return False


ans = []
for _ in range(tc):
    initialize()
    res = operate()
    ans.append("YES" if res else "NO")
print(*ans, sep='\n')
