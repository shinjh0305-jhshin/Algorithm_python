import sys
from collections import deque
Input = sys.stdin.readline
nodes = int(Input())
edges = int(Input())
graph = [[] for _ in range(nodes + 1)]
graphReverse = [[] for _ in range(nodes + 1)]
minimum = [0] * (nodes + 1)
nodeBefore = [0] * (nodes + 1)
for _ in range(edges):
    start, end, cost = map(int, Input().split())
    graph[start].append((end, cost))
    graphReverse[end].append((start, cost))
    nodeBefore[end] += 1
startNode, endNode = map(int, Input().split())
qu = deque()
qu.append(startNode)
minimum[startNode] = 0

# find max time
while qu:
    curNode = qu.popleft()
    for nextNode in graph[curNode]:
        minimum[nextNode[0]] = max(minimum[nextNode[0]], nextNode[1] + minimum[curNode])
        nodeBefore[nextNode[0]] -= 1
        if nodeBefore[nextNode[0]] == 0:
            qu.append(nextNode[0])

# find roads to take
roads = 0
visited = [False] * (nodes + 1)
qu.append(endNode)
while qu:
    curNode = qu.popleft()
    for beforeNode in graphReverse[curNode]:
        if minimum[beforeNode[0]] + beforeNode[1] == minimum[curNode]:
            roads += 1
            if not visited[beforeNode[0]]:
                qu.append(beforeNode[0])
                visited[beforeNode[0]] = True

print(minimum[endNode], roads, sep='\n')