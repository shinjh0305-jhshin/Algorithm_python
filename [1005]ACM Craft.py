import sys
from collections import deque
Input = sys.stdin.readline
tc = int(Input())
nodes, edges = 0, 0
in_nodes = []
cost = []
graph = []


def initialize():
    global nodes, edges, cost, graph, in_nodes
    nodes, edges = map(int, Input().split())
    cost = [0] + list(map(int, Input().split()))
    graph = [[] for _ in range(nodes + 1)]
    in_nodes = [0] * (nodes + 1)
    for _ in range(edges):
        s, e = map(int, Input().split())
        graph[s].append(e)
        in_nodes[e] += 1


def operate():
    ans = []
    for _ in range(tc):
        initialize()
        target = int(Input())
        min_time = [0] * (nodes + 1)
        qu = deque()

        for i in range(1, nodes + 1):
            if in_nodes[i] == 0:
                qu.append(i)

        while qu:
            cn = qu.popleft()
            if cn == target:
                ans.append(min_time[target] + cost[target])
                break
            for nn in graph[cn]:
                min_time[nn] = max(min_time[nn], min_time[cn] + cost[cn])
                in_nodes[nn] -= 1
                if in_nodes[nn] == 0:
                    qu.append(nn)
    print(*ans, sep='\n')


operate()
