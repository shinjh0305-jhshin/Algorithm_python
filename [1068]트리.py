import sys
Input = sys.stdin.readline
nodes = int(Input())
parent = list(map(int, Input().split()))
graph = [[] for _ in range(nodes)]
children = [0] * nodes
target = int(Input())
leaves = 0


def initialize():
    global leaves
    for i in range(nodes):
        if parent[i] >= 0:
            children[parent[i]] += 1
            graph[parent[i]].append(i)
    for i in children:
        if i == 0:
            leaves += 1


def is_leaf(i):
    return True if children[i] == 0 else False


def dfs(node):
    ans = 0
    if is_leaf(node):
        return 1
    for nn in graph[node]:
        ans += dfs(nn)
    return ans


def operate():
    initialize()

    global leaves
    if parent[target] == -1:
        leaves = 0
    else:
        if is_leaf(target):
            leaves -= 1
        else:
            leaves -= dfs(target)
        if children[parent[target]] == 1:
            leaves += 1
    print(leaves)


operate()