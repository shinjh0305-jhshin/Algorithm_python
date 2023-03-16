import sys
from collections import deque
Input = sys.stdin.readline
ladders, snakes = map(int, Input().split())
k = [0] * 101
visited = [False] * 101


def operate():
    for _ in range(ladders + snakes):
        x, y = map(int, Input().split())
        k[x] = y

    qu = deque([1])
    visited[1] = True
    ans = 1

    while True:
        len_qu = len(qu)
        for _ in range(len_qu):
            cn = qu.popleft()
            for i in range(1, 7):
                nn = cn + i
                if 1 < nn < 100 and not visited[nn]:
                    while k[nn]:  # 뱀, 사다리로 이동할 수 있는 만큼 계속 이동
                        visited[nn] = True
                        nn = k[nn]
                    visited[nn] = True  # 이동 종료 지점
                    qu.append(nn)
                if nn == 100:
                    print(ans)
                    return
        ans += 1


operate()
