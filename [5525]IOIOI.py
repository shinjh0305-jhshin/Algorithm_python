import sys
Input = sys.stdin.readline


def operate():
    sz = int(Input())
    length = int(Input())
    k = Input()
    res = [0] * length
    ans = 0
    for i in range(length):
        if k[i] == 'I':
            if i >= 2 and k[i - 2:i] == 'IO':
                res[i] = res[i - 2] + 1
                if res[i] >= sz:
                    ans += 1
            else:
                res[i] = 0
    print(ans)


operate()