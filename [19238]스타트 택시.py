import sys
from collections import deque
Input = sys.stdin.readline
sz, ppls, fuel = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
cx, cy = map(int, Input().split())
INF = 2134567890
ppl = {}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    global cx, cy
    cx, cy = cx - 1, cy - 1
    for _ in range(ppls):
        a, b, c, d = map(int, Input().split())
        ppl[(a - 1, b - 1)] = (c - 1, d - 1)


def find_customer():
    if (cx, cy) in ppl:
        return (cx, cy), 0
    qu = deque([[cx, cy]])
    visited = [[False] * sz for _ in range(sz)]
    visited[cx][cy] = True

    d = 1
    res = (INF, INF)
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            x, y = qu.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < sz and 0 <= ny < sz and k[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if (nx, ny) in ppl:
                        res = min(res, (nx, ny))
                    qu.append([nx, ny])
        if res[0] != INF:
            break
        d += 1
    return res, d


def dist_to_dest(p):
    qu = deque([p])
    visited = [[False] * sz for _ in range(sz)]
    target = ppl[p]

    ans = 1
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            x, y = qu.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (nx, ny) == target:
                    return ans
                if 0 <= nx < sz and 0 <= ny < sz and k[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    qu.append([nx, ny])
        ans += 1
    return INF


def operate():
    global fuel, cx, cy

    left_ppl = ppls
    while left_ppl:
        p, d1 = find_customer()
        if p == (INF, INF):  # 손님 있는 곳으로 이동 불가
            print(-1)
            return
        d2 = dist_to_dest(p)
        if d2 == INF:  # 목적지로 이동 불가
            print(-1)
            return
        if d1 + d2 > fuel:
            break
        fuel -= d1 + d2
        fuel += d2 * 2
        cx, cy = ppl[p]
        del ppl[p]
        left_ppl -= 1

    if left_ppl:
        print(-1)
    else:
        print(fuel)


initialize()
operate()
