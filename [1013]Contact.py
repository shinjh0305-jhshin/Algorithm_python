import re
import sys
Input = sys.stdin.readline
sz = int(Input())
k = [Input().rstrip() for _ in range(sz)]


def operate():
    for i in range(sz):
        p = re.compile('(100+1+|01)+')
        if p.fullmatch(k[i]):
            print('YES')
        else:
            print('NO')


operate()