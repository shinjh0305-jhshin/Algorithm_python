import sys
Input = sys.stdin.readline
nodes, changes, sums = map(int, Input().split())
rawdata = [0] * nodes
segTree = [0] * (4 * nodes)


def make_tree(node=1, start=0, end=nodes - 1):
    if start == end:
        segTree[node] = rawdata[start]
    else:
        segTree[node] = make_tree(node * 2, start, (start + end) // 2) + \
                        make_tree(node * 2 + 1, (start + end) // 2 + 1, end)
    return segTree[node]


# [start, end] : node의 구간, [left, right] : 합을 구하는 구간
def get_sum(left, right, start=0, end=nodes - 1, node=1):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return segTree[node]
    return get_sum(left, right, start, (start + end) // 2, node * 2) + \
        get_sum(left, right, (start + end) // 2 + 1, end, node * 2 + 1)


def update(idx, diff, start=0, end=nodes - 1, node=1):
    if idx < start or end < idx:
        return

    if start == end:
        segTree[node] += diff
    elif start != end:
        update(idx, diff, start, (start + end) // 2, node * 2)
        update(idx, diff, (start + end) // 2 + 1, end, node * 2 + 1)
        segTree[node] = segTree[node * 2] + segTree[node * 2 + 1]


def initialize():
    for i in range(nodes):
        rawdata[i] = int(Input())
    make_tree()


def operate():
    initialize()
    for _ in range(changes + sums):
        op, x, y = map(int, Input().split())
        if op == 1:  # change rawdata[x] to y
            x -= 1
            update(x, y - rawdata[x])
            rawdata[x] = y
        else:  # get sum from x to y
            print(get_sum(x - 1, y - 1))


operate()
