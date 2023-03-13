n, p, q = map(int, input().split())
dp = {0: 1}


def find(num):
    if dp.get(num, -1) == -1:
        dp[num] = find(num // p) + find(num // q)
    return dp[num]


print(find(n))
