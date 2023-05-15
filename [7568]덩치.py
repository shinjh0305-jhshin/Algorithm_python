import sys
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]


def operate():
    order = [0] * sz
    for i in range(sz):
        for j in range(i + 1, sz):
            if k[i][0] < k[j][0] and k[i][1] < k[j][1]:
                order[i] += 1
            elif k[i][0] > k[j][0] and k[i][1] > k[j][1]:
                order[j] += 1
    print(*list(map(lambda x: x + 1, order)))


operate()
