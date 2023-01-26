import sys
Input = sys.stdin.readline
nodes = int(Input())
tree = {}
for _ in range(nodes):
    root, left, right = Input().split()
    tree[root] = [left, right]


def pre_order(cn):
    if cn == '.':
        return
    print(cn, end='')
    pre_order(tree[cn][0])
    pre_order(tree[cn][1])


def in_order(cn):
    if cn == '.':
        return
    in_order(tree[cn][0])
    print(cn, end='')
    in_order(tree[cn][1])


def post_order(cn):
    if cn == '.':
        return
    post_order(tree[cn][0])
    post_order(tree[cn][1])
    print(cn, end='')


pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()