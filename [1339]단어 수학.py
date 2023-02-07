import sys
Input = sys.stdin.readline
sz = int(Input())
rawdata = [Input().rstrip() for _ in range(sz)]
result = {}


def make_weight(target):
    len_t = len(target)
    weight = 10 ** (len_t - 1)
    for k in target:
        if k in result:
            result[k] += weight
        else:
            result[k] = weight
        weight //= 10


def operate():
    for i in range(sz):
        make_weight(rawdata[i])
    res = sorted(result.items(), key=lambda x: x[1], reverse=True)
    ans = 0
    num = 9
    for i in range(len(res)):
        ans += res[i][1] * num
        num -= 1
    print(ans)


operate()
