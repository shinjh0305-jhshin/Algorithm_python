from collections import deque
sz = int(input())
visited = [[False] * 1000 for _ in range(1000)]


def operate():
    qu = deque([[1, 0]])  # 현재 이모티콘, 클립보드 이모티콘
    visited[1][0] = True

    ans = 1
    while True:
        len_qu = len(qu)
        for _ in range(len_qu):
            x, y = qu.popleft()
            nn = [[x, x], [x + y, y], [x - 1, y]]
            for nx, ny in nn:
                if nx == sz:
                    print(ans)
                    return
                if 0 <= nx < 1000 and 0 <= ny < 1000 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    qu.append([nx, ny])
        ans += 1


operate()

