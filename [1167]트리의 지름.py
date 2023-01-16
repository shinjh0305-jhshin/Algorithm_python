import sys
from collections import deque

Input = sys.stdin.readline
nodes = int(Input())

graph = [[] for _ in range(nodes + 1)]
for i in range(1, nodes + 1):
    tmp = list(map(int, Input().split()))
    curNode = tmp[0]
    for j in range(1, len(tmp) - 1, 2):
        graph[curNode].append((tmp[j], tmp[j + 1]))


def bfs(startNode):
    visited[startNode[0]] = True
    qu = deque()
    qu.append(startNode)  # (node, dist)
    maxNode = (0, 0)

    while qu:
        cur = qu.popleft()
        curNode = cur[0]
        curDist = cur[1]
        for i in graph[curNode]:
            nextNode = i[0]
            nextDist = curDist + i[1]
            if not visited[nextNode]:
                visited[nextNode] = True
                qu.append((nextNode, nextDist))
                if nextDist > maxNode[1]:
                    maxNode = (nextNode, nextDist)

    return maxNode


visited = [False] * (nodes + 1)
maxOne = bfs((1, 0))
visited = [False] * (nodes + 1)
print(bfs((maxOne[0], 0))[1])