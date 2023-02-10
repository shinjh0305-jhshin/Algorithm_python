import sys
Input = sys.stdin.readline
sz = int(Input())
k = [list(Input().split()) for _ in range(sz)]
res = {}


def make_tree(target, data):
    if data not in target:
        target[data] = {}


def print_tree(target, depth):
    for x in sorted(target.keys()):
        ans = []
        for _ in range(depth * 2):
            ans.append('-')
        ans.append(x)
        print(*ans, sep='')
        print_tree(target[x], depth + 1)


def operate():
    for x in range(sz):
        it = int(k[x][0])
        cur_dict = res
        for i in range(1, it + 1):
            data = k[x][i]
            make_tree(cur_dict, data)
            cur_dict = cur_dict[data]
    print_tree(res, 0)


operate()
