from collections import deque
from itertools import combinations
k = [list(input()) for _ in range(5)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def check_connected(x):
    qu = deque([x[0]])
    visited = [False] * 7
    left = 6
    visited[0] = True

    while qu:
        c = qu.popleft()
        cx, cy = c // 5, c % 5
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                el = nx * 5 + ny
                try:
                    idx = x.index(el)
                    if not visited[idx]:
                        visited[idx] = True
                        left -= 1
                        qu.append(el)
                except ValueError:
                    continue
    if left:
        return False
    else:
        return True


def operate():
    ans = 0
    for tmp in combinations(range(25), 7):
        if check_connected(tmp):
            S, Y = 0, 0
            for i in tmp:
                if k[i // 5][i % 5] == 'S':
                    S += 1
                else:
                    Y += 1
            if S >= 4:
                ans += 1
    print(ans)


operate()
