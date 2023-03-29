from itertools import combinations
k = []
ans = []


def initialize():
    k.clear()
    tmp = list(map(int, input().split()))
    for i in range(0, 18, 3):
        k.append(tmp[i:i+3])
        if sum(k[-1]) != 5:
            return False
    return True


def change_status(i_win, tie, i_loose, chg):
    for i in i_win:
        k[i][2] += chg
    for i in tie:
        k[i][1] += chg
    for i in i_loose:
        k[i][0] += chg


def is_possible(idx=0):
    if idx == 5:
        return True

    for i_win in combinations(range(idx + 1, 6), k[idx][0]):
        avail = list(filter(lambda x: k[x][2], i_win))  # 선택된 팀들이 질 수 없는 상황일 경우
        if len(avail) != len(i_win):
            continue
        left_team = list(filter(lambda x: x not in i_win, range(idx + 1, 6)))

        for tie in combinations(left_team, k[idx][1]):  # 비길 수 없다
            avail = list(filter(lambda x: k[x][1], tie))
            if len(avail) != len(tie):
                continue
            left_left_team = list(filter(lambda x: x not in tie, left_team))

            for i_loose in combinations(left_left_team, k[idx][2]):  # 질 수 없다
                avail = list(filter(lambda x: k[x][0], i_loose))
                if len(avail) != len(i_loose):
                    continue

                change_status(i_win, tie, i_loose, -1)  # 승부 반영한다
                res = is_possible(idx + 1)
                if res:
                    return True
                change_status(i_win, tie, i_loose, 1)  # 승부 다시 원래대로(백트래킹)

    return False


def operate():
    ans.append(int(is_possible()))


for _ in range(4):
    res = initialize()
    if res:
        operate()
    else:
        ans.append(0)

print(*ans, sep=' ')
