
from collections import deque
k = input().rstrip()
pair = []
ans = set()
tmp = [True] * len(k)
first_to_visit = True  # 없앤 괄호가 없다.


def initialize():
    qu = deque()
    for x in range(len(k)):
        if k[x] == '(':
            qu.append(x)
        elif k[x] == ')':
            pair.append((qu.pop(), x))


def dfs(i=0):
    if i < len(pair):
        tmp[pair[i][0]] = tmp[pair[i][1]] = True
        dfs(i + 1)
        tmp[pair[i][0]] = tmp[pair[i][1]] = False
        dfs(i + 1)
    else:
        global first_to_visit
        if first_to_visit:
            first_to_visit = not first_to_visit
        else:
            res = []
            for i in range(len(k)):
                if tmp[i]:
                    res.append(k[i])
            ans.add(''.join(res))


def operate():
    dfs()
    global ans
    ans = list(ans)
    ans.sort()
    print(*ans, sep='\n')


initialize()
operate()
