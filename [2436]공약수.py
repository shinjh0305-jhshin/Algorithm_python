import math
a, b = map(int, input().split())


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def operate():
    divided = b // a

    tmp = [2134567890, 2134567890]
    for i in range(1, math.trunc(math.sqrt(divided)) + 1):
        if divided % i == 0:
            j = divided // i
            if gcd(i, j) == 1 and sum(tmp) > sum([i, j]):
                tmp = [i, j]

    print(a * tmp[0], a * tmp[1])


operate()
