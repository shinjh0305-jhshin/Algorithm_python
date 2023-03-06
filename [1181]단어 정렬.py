import sys
Input = sys.stdin.readline
sz = int(Input())
k = [Input().rstrip() for _ in range(sz)]


def operate():
    ans = list(set(k))
    ans.sort(key=lambda x: (len(x), x))
    print(*ans, sep='\n')


operate()
