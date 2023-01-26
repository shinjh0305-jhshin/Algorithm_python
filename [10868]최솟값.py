import sys
Input = sys.stdin.readline
nodes, queries = map(int, Input().split())
rawdata = [0] * nodes
segTree = [0] * (4 * nodes)
INF = 2134567890


def make_tree(node=1, left=0, right=nodes - 1):
    if left == right:
        segTree[node] = rawdata[left]
    else:
        segTree[node] = min(make_tree(node * 2, left, (left + right) // 2),
                            make_tree(node * 2 + 1, (left + right) // 2 + 1, right))
    return segTree[node]


def get_min(start, end, left=0, right=nodes - 1, node=1):  # s,e:tosearch, l,r:node
    if end < left or right < start:
        return INF
    if start <= left and right <= end:
        return segTree[node]
    return min(get_min(start, end, left, (left + right) // 2, node * 2),
               get_min(start, end, (left + right) // 2 + 1, right, node * 2 + 1))


def initialize():
    for i in range(nodes):
        rawdata[i] = int(Input())
    make_tree()


def operate():
    initialize()
    for _ in range(queries):
        x, y = map(int, Input().split())
        print(get_min(x - 1, y - 1))


operate()
