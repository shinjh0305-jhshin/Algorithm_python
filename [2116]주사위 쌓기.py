import sys
Input = sys.stdin.readline
sz = int(Input())
dice = [list(map(int, Input().split())) for _ in range(sz)]
pair = [5, 3, 4, 1, 2, 0]
max_num = [[0] * 6 for _ in range(sz)]


def initialize():
    for i in range(sz):
        for j in range(3):
            for k in range(6):
                if k != j and k != pair[j]:
                    max_num[i][j] = max(max_num[i][j], dice[i][k])
                max_num[i][pair[j]] = max_num[i][j]


def make_block(idx):
    ans = 0
    for i in range(sz):
        ans += max_num[i][idx]

        if i < sz - 1:
            pair_num = dice[i][pair[idx]]
            idx = dice[i + 1].index(pair_num)

    return ans


def operate():
    ans = 0
    for i in range(6):
        ans = max(ans, make_block(i))
    print(ans)


initialize()
operate()
