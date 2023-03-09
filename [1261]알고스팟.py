import sys
from heapq import heappop, heappush
Input = sys.stdin.readline
cols, rows = map(int, Input().split())
k = [list(map(int, Input().rstrip())) for _ in range(rows)]
dp = [[sys.maxsize] * cols for _ in range(rows)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def dijkstra():
    pq = []
    heappush(pq, (0, 0, 0))  # 파괴, row, col
    dp[0][0] = 0

    while pq:
        cd, cx, cy = heappop(pq)
        if dp[cx][cy] < cd:
            continue
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                if k[nx][ny]:
                    nd = cd + 1
                else:
                    nd = cd
                if dp[nx][ny] > nd:
                    dp[nx][ny] = nd
                    heappush(pq, (nd, nx, ny))


def operate():
    dijkstra()
    print(dp[rows - 1][cols - 1])


operate()
