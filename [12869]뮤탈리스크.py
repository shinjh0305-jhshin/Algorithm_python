from collections import deque
from itertools import permutations
sz = int(input())
k = list(map(int, input().split()))
visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
dec = [9, 3, 1]


def operate():
    qu = deque()
    qu.append(k + [0] * (3 - sz))
    visited[qu[0][0]][qu[0][1]][qu[0][2]] = True

    ans = 1
    while True:
        len_qu = len(qu)
        for _ in range(len_qu):
            cur = qu.popleft()
            for order in permutations(range(sz), sz):
                nn = cur[:]
                for i in range(sz):
                    idx = order[i]
                    if nn[idx] - dec[i] > 0:
                        nn[idx] -= dec[i]
                    else:
                        nn[idx] = 0
                if nn == [0, 0, 0]:
                    return ans
                x, y, z = nn
                if not visited[x][y][z]:
                    visited[x][y][z] = True
                    qu.append([x, y, z])
        ans += 1


print(operate())