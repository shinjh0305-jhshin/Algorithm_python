import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
sz = int(Input())
ppl = [0] + list(map(int, Input().split()))
k = [[] for _ in range(sz + 1)]
dp = [[] for _ in range(sz + 1)]  # choose, not choose


def initialize():
    for _ in range(sz - 1):
        x, y = map(int, Input().split())
        k[x].append(y)
        k[y].append(x)


def dfs(n=1, parent=0):
    if len(k[n]) == 1 and k[n][0] == parent:  # leaf node
        dp[n] = [ppl[n], 0]
        return
    for nn in k[n]:
        if nn != parent:
            dfs(nn, n)

    tmp = [0, 0]  # choose, not choose
    # Choose
    for nn in k[n]:
        if nn == parent:
            continue
        tmp[0] += dp[nn][1]
    tmp[0] += ppl[n]
    # Not choose
    for nn in k[n]:
        if nn == parent:
            continue
        tmp[1] += max(dp[nn])
    dp[n] = tmp


def operate():
    dfs()
    print(max(dp[1]))


initialize()
operate()
