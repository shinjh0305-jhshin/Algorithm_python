import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
sz, k = 0, []


def dijkstra():
    visited = [[sys.maxsize] * sz for _ in range(sz)]
    pq = []
    visited[0][0] = k[0][0]
    heappush(pq, [0, 0, k[0][0]])

    while True:
        x, y, c = heappop(pq)

        if [x, y] == [sz - 1, sz - 1]:
            return c
        if visited[x][y] < c:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < sz and 0 <= ny < sz:
                nc = c + k[nx][ny]
                if visited[nx][ny] > nc:
                    visited[nx][ny] = nc
                    heappush(pq, [nx, ny, nc])


def operate():
    global sz, k
    t = 1
    while True:
        sz = int(Input())
        if sz == 0:
            return
        k = [list(map(int, Input().split())) for _ in range(sz)]
        ans = dijkstra()
        print(f'Problem {t}: {ans}')
        t += 1

operate()
