import sys
Input = sys.stdin.readline
sz_tmp, chg = map(int, Input().split())
tmp = [int(Input()) for _ in range(sz_tmp)]
k, sz = [], 0
dp = []


def initialize():
    global k, sz, dp
    cur_num = tmp[0]
    length = 1

    for next_num in tmp[1:]:
        if cur_num == next_num:
            length += 1
        else:
            k.append(length)
            cur_num = next_num
            length = 1
    k.append(length)
    sz = len(k)
    dp = [[0] * sz for _ in range(chg + 1)]


def operate():
    for j in range(sz - 1, -1, -1):
        for i in range(chg + 1):
            if j == sz - 1:
                dp[i][j] = k[j]

            else:
                change = k[j]
                if i > 0:
                    change += dp[i - 1][j + 1]

                no_change = k[j]
                if j < sz - 2:
                    no_change += dp[i][j + 2]

                dp[i][j] = max(change, no_change)

    if tmp[0] == 2:
        ans = max(dp[chg - 1][0], dp[chg][1] if sz > 1 else 0)
    else:
        ans = dp[chg][0]
    print(ans)


initialize()
operate()
