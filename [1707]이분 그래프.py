import sys
from collections import deque
Input = sys.stdin.readline


def bfs(node):
    qu = deque()
    qu.append(node)
    visited[node] = True

    while qu:
        curnode = qu.popleft()
        for nextnode in graph[curnode]:
            if visited[nextnode] and group[nextnode] == group[curnode]:
                return False
            elif not visited[nextnode]:
                visited[nextnode] = True
                group[nextnode] = (group[curnode] + 1) % 2
                qu.append(nextnode)
    return True


tc = int(Input())
for _1 in range(tc):
    nodes, edges = map(int, Input().split())
    graph = [[] for _3 in range(nodes + 1)]
    visited = [False] * (nodes + 1)
    group = [0] * (nodes + 1)
    for _2 in range(edges):
        start, end = map(int, Input().split())
        graph[start].append(end)
        graph[end].append(start)
    flag = True
    for node in range(1, nodes + 1):
        if not visited[node]:
            if not bfs(node):
                flag = False
                break;

    if not flag:
        print("NO")
    else:
        print("YES")