import sys
sys.setrecursionlimit(10 ** 6)
seq = list(map(int, input().split()))
seq.pop(-1)
dp = [[[0] * 5 for _ in range(5)] for _ in range(len(seq))]


def mov_cost(a, b):  # moving cost from a to b
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif (a - b) ** 2 == 4:
        return 4
    else:
        return 3


def mov_foot(idx=0, lfoot=0, rfoot=0):
    if idx == len(seq):
        return 0
    elif dp[idx][lfoot][rfoot]:
        return dp[idx][lfoot][rfoot]
    nfoot = seq[idx]
    res = min(mov_foot(idx + 1, nfoot, rfoot) + mov_cost(lfoot, nfoot),
              mov_foot(idx + 1, lfoot, nfoot) + mov_cost(rfoot, nfoot))
    dp[idx][lfoot][rfoot] = res
    return res


print(mov_foot())