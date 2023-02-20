import sys
sys.setrecursionlimit(10 ** 6)

k = input().rstrip()
mod = 1000000
len_k = len(k)
dp = [sys.maxsize] * len_k


def dfs(idx):
    if k[idx] == '0':
        dp[idx] = 0
        return
    if idx == len_k - 1:
        dp[idx] = 1
        return
    # 1자릿수
    if dp[idx + 1] == sys.maxsize:
        dfs(idx + 1)
    dp[idx] = dp[idx + 1]
    # 2자릿수
    if int(k[idx:idx + 2]) <= 26:
        if idx == len_k - 2:
            dp[idx] += 1
        else:
            if dp[idx + 2] == sys.maxsize:
                dfs(idx + 2)
            dp[idx] += dp[idx + 2]
    dp[idx] %= mod


def operate():
    dfs(0)
    print(dp[0])


operate()
