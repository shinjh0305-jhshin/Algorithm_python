from collections import deque
capa = list(map(int, input().split()))  # capacity
visited = [[False for i in range(201)] for j in range(201)]


def bfs():
    qu = deque()
    qu.append([0, 0, capa[2]])
    visited[0][0] = True

    while qu:
        cur = qu.popleft()
        for x in range(3):
            target = [(x + 1) % 3, (x + 2) % 3]
            for y in target:
                new = cur.copy()
                if capa[y] >= cur[x] + cur[y]:
                    new[x] = 0
                    new[y] = cur[x] + cur[y]
                else:
                    new[x] -= capa[y] - cur[y]
                    new[y] = capa[y]
                if not visited[new[0]][new[1]]:
                    qu.append(new)
                    visited[new[0]][new[1]] = True
                    if new[0] == 0:
                        case_A.add(new[2])


case_A = set()
case_A.add(capa[2])
bfs()
print(*sorted(case_A))