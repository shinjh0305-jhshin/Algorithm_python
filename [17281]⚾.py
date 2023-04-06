import sys
from itertools import permutations
Input = sys.stdin.readline
innings = int(Input())
inning = [list(map(int, Input().split())) for _ in range(innings)]


def play(order):
    score = 0
    p_idx = 0

    for inn in range(innings):
        outs = 0
        b1, b2, b3 = 0, 0, 0
        while outs < 3:
            player = order[p_idx]
            res = inning[inn][player]
            if res == 0:
                outs += 1
            elif res == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif res == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif res == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            p_idx = (p_idx + 1) % 9

    return score


def operate():
    ans = -1
    for tmp_order in permutations(range(1, 9)):
        order = list(tmp_order)
        order.insert(3, 0)
        ans = max(ans, play(order))
    print(ans)


operate()
