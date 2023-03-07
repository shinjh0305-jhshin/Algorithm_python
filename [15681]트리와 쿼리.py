import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
nodes, root, queries = map(int, Input().split())
k = [[] for _ in range(nodes + 1)]
dp = [0] * (nodes + 1)
visited = [False] * (nodes + 1)


def initialize():
    for _ in range(nodes - 1):
        x, y = map(int, Input().split())
        k[x].append(y)
        k[y].append(x)


def count_children(cn):
    visited[cn] = True
    for nn in k[cn]:
        if not visited[nn]:
            dp[cn] += (count_children(nn) + 1)
    return dp[cn]


def operate():
    ans = []
    for _ in range(queries):
        q = int(Input())
        ans.append(dp[q] + 1)
    print(*ans, sep='\n')


initialize()
count_children(root)
operate()
