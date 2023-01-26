import sys
Input = sys.stdin.readline
nodes, changes, muls = map(int, Input().split())
rawdata = [0] * nodes
segTree = [0] * (nodes * 4)
mod = 1000000007


def make_tree(node=1, left=0, right=nodes - 1):
    if left == right:
        segTree[node] = rawdata[left]
    else:
        segTree[node] = (make_tree(node * 2, left, (left + right) // 2) *
                         make_tree(node * 2 + 1, (left + right) // 2 + 1, right)) % mod
    return segTree[node]


def make_mul(start, end, left=0, right=nodes-1, node=1):
    if end < left or right < start:
        return 1
    if start <= left and right <= end:
        return segTree[node]
    return (make_mul(start, end, left, (left + right) // 2, node * 2) *
            make_mul(start, end, (left + right) // 2 + 1, right, node * 2 + 1)) % mod


def change_num(idx, value, left=0, right=nodes - 1, node=1):
    if idx < left or right < idx:
        return
    if left == right:
        segTree[node] = value
        return
    if left != right:
        change_num(idx, value, left, (left + right) // 2, node * 2)
        change_num(idx, value, (left + right) // 2 + 1, right, node * 2 + 1)
    segTree[node] = (segTree[node * 2] * segTree[node * 2 + 1]) % mod


def initialize():
    for i in range(nodes):
        rawdata[i] = int(Input())
    make_tree()


def operate():
    initialize()
    for _ in range(muls + changes):
        op, x, y = map(int, Input().split())
        if op == 1:  # change rawdata[x] to y
            change_num(x - 1, y)
            rawdata[x - 1] = y
        else:
            print(make_mul(x - 1, y - 1))


operate()