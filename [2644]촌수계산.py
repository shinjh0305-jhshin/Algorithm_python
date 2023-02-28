import sys
from collections import deque
Input = sys.stdin.readline
ppls = int(Input())
x, y = map(int, Input().split())
rels = int(Input())
graph = [[] for _ in range(ppls + 1)]


def initialize():
    for _ in range(rels):
        a, b = map(int, Input().split())
        graph[a].append(b)
        graph[b].append(a)


def operate():
    qu = deque()
    visited = [False] * (ppls + 1)
    qu.append(x)
    visited[x] = True

    ans = 1
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cn = qu.popleft()
            for nn in graph[cn]:
                if not visited[nn]:
                    if nn == y:
                        print(ans)
                        return
                    visited[nn] = True
                    qu.append(nn)
        ans += 1
    print(-1)


initialize()
operate()
