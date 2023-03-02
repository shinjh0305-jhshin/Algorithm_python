weights = int(input())
weight = list(map(int, input().split()))
marbles = int(input())
marble = list(map(int, input().split()))
dp = [[False] * 15001 for _ in range(31)]


def make_weight(cnt=0, res=0):
    if dp[cnt][res]:
        return

    dp[cnt][res] = True

    if cnt >= weights:
        return

    make_weight(cnt + 1, res + weight[cnt])
    make_weight(cnt + 1, res)
    make_weight(cnt + 1, abs(res - weight[cnt]))


def operate():
    make_weight()
    ans = []
    for m in marble:
        if m > 15000:
            ans.append('N')
        elif dp[weights][m]:
            ans.append('Y')
        else:
            ans.append('N')
    print(*ans)


operate()


