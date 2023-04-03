import sys
Input = sys.stdin.readline
sz = int(Input())
cost = [0] + list(map(int, Input().split()))
k = [[] for _ in range(sz + 1)]
visited = [False] * (sz + 1)
dp = [[0, 0] for _ in range(sz + 1)]  # O / X
ans = 0
seq = []


def initialize():
    for _ in range(sz - 1):
        x, y = map(int, Input().split())
        k[x].append(y)
        k[y].append(x)


def dfs(cn=1, pn=0):
    if len(k[cn]) == 1 and k[cn][0] == pn:
        dp[cn] = [cost[cn], 0]
        return

    dp[cn][0] = cost[cn]
    for nn in k[cn]:
        if nn != pn:
            dfs(nn, cn)
            dp[cn][0] += dp[nn][1]
            dp[cn][1] += max(dp[nn][0], dp[nn][1])


def get_seq(cn=1, prev=False, pn=0):
    if not prev and dp[cn][0] > dp[cn][1]:
        cur = True
        seq.append(cn)
    else:
        cur = False
    for nn in k[cn]:
        if nn == pn:
            continue
        get_seq(nn, cur, cn)


def operate():
    dfs()
    get_seq()
    seq.sort()

    print(max(dp[1]))
    print(*seq)


initialize()
operate()
