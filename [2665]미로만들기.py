import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().rstrip())) for _ in range(sz)]
visited = [[sys.maxsize] * sz for _ in range(sz)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def operate():
    pq = []
    visited[0][0] = 0
    heappush(pq, [0, 0, 0])

    while True:
        cc, cx, cy = heappop(pq)
        if visited[cx][cy] < cc:
            continue
        for i in range(4):
            nx, ny, nc = cx + dx[i], cy + dy[i], cc
            if nx == sz - 1 and ny == sz - 1:
                return nc
            if 0 <= nx < sz and 0 <= ny < sz:
                if k[nx][ny] == 0:
                    nc += 1
                if visited[nx][ny] > nc:
                    visited[nx][ny] = nc
                    heappush(pq, [nc, nx, ny])


print(operate())
