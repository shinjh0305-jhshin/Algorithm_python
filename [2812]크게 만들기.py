from collections import deque
len_k, erase = map(int, input().split())
k = list(map(int, input().rstrip()))


def operate():
    global erase
    qu = deque()
    for i in range(len_k):
        cn = k[i]
        while qu and erase and qu[-1] < cn:
            qu.pop()
            erase -= 1
        qu.append(cn)
    while erase:
        qu.pop()
        erase -= 1
    print(*qu, sep='')


operate()
