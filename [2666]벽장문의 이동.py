import sys
sys.setrecursionlimit(10 ** 9)
Input = sys.stdin.readline
sz = int(Input())
a, b = map(int, Input().split())
targets = int(Input())
target = [int(Input()) for _ in range(targets)]


def dfs(x, y, depth):
    if depth == targets:
        return 0

    tmp1 = abs(x - target[depth]) + dfs(target[depth], y, depth + 1)
    tmp2 = abs(y - target[depth]) + dfs(x, target[depth], depth + 1)

    return min(tmp1, tmp2)


def operate():
    print(dfs(a, b, 0))


operate()