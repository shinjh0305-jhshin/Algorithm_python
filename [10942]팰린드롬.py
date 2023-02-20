import sys
Input = sys.stdin.readline
sz = int(Input())
k = list(map(int, Input().split()))
dp = [[True] * sz for _ in range(sz)]


def initialize():
    for d in range(1, sz):
        for i in range(0, sz - d):
            j = i + d
            if k[i] != k[j] or (d >= 2 and not dp[i + 1][j - 1]):
                dp[i][j] = False

def operate():
    q = int(Input())
    ans = []
    for _ in range(q):
        qx, qy = map(int, Input().split())
        ans.append(int(dp[qx - 1][qy - 1]))
    print(*ans, sep='\n')


initialize()
operate()