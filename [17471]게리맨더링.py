import sys
from collections import deque
from itertools import combinations
Input = sys.stdin.readline
sz = int(Input())
ppls = [0] + list(map(int, Input().split()))
graph = [[] for _ in range(sz + 1)]


def initialize():
    for i in range(1, sz + 1):
        tmp = list(map(int, Input().split()))
        for x in range(1, len(tmp)):
            graph[i].append(tmp[x])


def is_connected(x):
    visited = [False] * (sz + 1)
    left_node = len(x) - 1
    qu = deque()
    qu.append(x[0])
    visited[x[0]] = True

    while qu:
        cn = qu.popleft()
        for nn in graph[cn]:
            if nn in x and not visited[nn]:
                visited[nn] = True
                left_node -= 1
                qu.append(nn)

    return False if left_node else True


def operate():
    ans = sys.maxsize
    for i in range(0, sz - 1):  # i : 1번이랑 같이 선거구에 묶일 구역의 수
        for with_1 in combinations(range(2, sz + 1), i):
            with_1 = set(with_1)
            without_1 = set(range(2, sz + 1)) - with_1

            if is_connected([1] + list(with_1)) and is_connected(list(without_1)):
                with_1_ppls = ppls[1]
                without_1_ppls = 0
                for x in range(2, sz + 1):
                    if x in with_1:
                        with_1_ppls += ppls[x]
                    else:
                        without_1_ppls += ppls[x]
                ans = min(ans, abs(with_1_ppls - without_1_ppls))
    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)


initialize()
operate()
