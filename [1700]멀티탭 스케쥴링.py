from collections import deque
tabs, sz = map(int, input().split())
k = list(map(int, input().split()))
tab = []
job = [deque() for _ in range(sz + 1)]


def initialize():
    for i in range(sz):
        job[k[i]].append(i)
    for i in range(sz + 1):
        job[i].append(sz + 100)  # 적당히 큰 수


def operate():
    ans = 0
    for x in k:
        if x in tab:
            job[x].popleft()
            continue
        elif len(tab) < tabs:
            tab.append(x)
        else:
            min_priority = job[tab[0]][0]
            min_priority_tab = 0
            for y in range(1, len(tab)):
                if job[tab[y]][0] > min_priority:
                    min_priority = job[tab[y]][0]
                    min_priority_tab = y
            tab[min_priority_tab] = x
            ans += 1
        job[x].popleft()
    print(ans)


initialize()
operate()