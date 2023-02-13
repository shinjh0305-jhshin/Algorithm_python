import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
G = int(Input())
P = int(Input())
planes = [int(Input()) for _ in range(P)]
root = [-1] * (G + 1)


def get_avail(cn):
    if root[cn] == -1:
        root[cn] = cn - 1
    else:
        root[cn] = get_avail(root[cn])
    return root[cn]


def operate():
    for i in range(P):
        if get_avail(planes[i]) == -1:
            print(i)
            return
    print(P)


operate()
