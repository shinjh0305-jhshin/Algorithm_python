import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]
dp = [[[-1] * 3 for _ in range(sz)] for _ in range(sz)]
dx, dy = [0, 1, 1], [1, 1, 0]  # 방향 별 이동량
to_check = [[0], [0, 1, 2], [2]]  # 방향 별 체크해야 하는 칸
avail = [[0, 1], [0, 1, 2], [1, 2]]  # 현재 방향에서 움직일 수 있는 방향


def dfs(i=0, j=0, d=0):
    cx, cy = i + dx[d], j + dy[d]
    if [cx, cy] == [sz - 1, sz - 1]:
        dp[i][j][d] = 1
        return 1
    ret = 0

    for nd in avail[d]:
        possible = True

        for td in to_check[nd]:
            tx, ty = cx + dx[td], cy + dy[td]
            if not (0 <= tx < sz and 0 <= ty < sz and k[tx][ty] == 0):
                possible = False
                break
        if not possible:
            continue

        ret += dfs(cx, cy, nd) if dp[cx][cy][nd] == -1 else dp[cx][cy][nd]

    dp[i][j][d] = ret
    return ret


def operate():
    print(dfs())


operate()
