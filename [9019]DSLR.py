import sys
from collections import deque
Input = sys.stdin.readline
tc = int(Input())
op = ['D', 'S', 'L', 'R']


def operate():
    a, b = map(int, Input().split())
    visited = [False] * 10001
    visited[a] = True

    qu = deque()
    qu.append((a, ""))
    while True:
        len_qu = len(qu)
        for _ in range(len_qu):
            cn, cs = qu.popleft()

            tmp = [(cn * 2) % 10000, (cn - 1) % 10000, (cn % 1000) * 10 + cn // 1000, (cn % 10) * 1000 + cn // 10]

            for i in range(4):
                ns = cs + op[i]
                if tmp[i] == b:
                    print(ns)
                    return
                else:
                    if not visited[tmp[i]]:
                        visited[tmp[i]] = True
                        qu.append((tmp[i], ns))


for _ in range(tc):
    operate()
