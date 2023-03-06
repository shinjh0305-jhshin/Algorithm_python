import sys

k = input()
sz_k = len(k)
dp = [[False] * sz_k for _ in range(sz_k)]
sz_palindrome = [0] * (sz_k + 1)


def operate():
    for i in range(sz_k):
        dp[i][i] = True
    for i in range(sz_k - 1):
        if k[i] == k[i + 1]:
            dp[i][i + 1] = True
    for l in range(2, sz_k):
        for i in range(0, sz_k - l):
            j = i + l
            if k[i] == k[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

    for e in range(1, sz_k + 1):
        sz_palindrome[e] = sys.maxsize
        for s in range(1, e + 1):
            if dp[s - 1][e - 1]:
                sz_palindrome[e] = min(sz_palindrome[e], sz_palindrome[s - 1] + 1)

    print(sz_palindrome[sz_k])


operate()
