import sys
Input = sys.stdin.readline
sz = int(Input())
rawdata = [[0, 0]] * (sz + 1)  # time, price
result = [0] * (sz + 2)
for i in range(1, sz + 1):
    rawdata[i] = list(map(int, Input().split()))


def operate():
    cur_max = 0
    for n in range(sz, 0, -1):
        ends_at = n + rawdata[n][0]
        if ends_at > sz + 1:  # 퇴사일에 마지막 상담 끝남
            result[n] = cur_max
        else:
            cur_max = max(cur_max, rawdata[n][1] + result[ends_at])
            result[n] = cur_max
    print(cur_max)


operate()
