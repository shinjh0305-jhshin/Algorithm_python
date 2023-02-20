import sys
Input = sys.stdin.readline
tc = int(Input())
sz, k, dp = 0, 0, 0


def get_min(x, y):
    if x == y:
        dp[x][y] = 0
    elif x + 1 == y:
        dp[x][y] = k[x] + k[y]
    elif dp[x][y] != sys.maxsize:
        return dp[x][y]
    else:
        range_sum = sum(k[x:y + 1])
        for i in range(x, y):
            dp[x][y] = min(dp[x][y],
                           get_min(x, i) + get_min(i + 1, y) + range_sum)
    return dp[x][y]


def operate():
    global sz, k, dp
    sz = int(Input())
    k = list(map(int, Input().split()))
    dp = [[sys.maxsize] * sz for _ in range(sz)]
    print(get_min(0, sz - 1))


for _ in range(tc):
    operate()
