import sys
from collections import Counter
Input = sys.stdin.readline
k = []


def operate():
    while True:
        t = Input().rstrip()
        if not t:
            break
        k.append(t)
    cnt = Counter(k)
    tot = len(k)
    ans = sorted(cnt.items())
    for i, j in ans:
        print(f'{i}{((j / tot) * 100): .4f}')


operate()
