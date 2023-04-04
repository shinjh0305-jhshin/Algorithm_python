from collections import deque, defaultdict
tc = int(input())
rows, cols, t = 0, 0, 0
ori_k = []
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
die = []
spread = defaultdict(lambda: set())
alive = 0


def initialize():
    global rows, cols, t, ori_k, alive, die
    rows, cols, t = map(int, input().split())
    ori_k = deque(deque(map(int, input().split())) for _ in range(rows))

    alive = 0
    spread.clear()
    die = [0] * (t + 1)

    for i in range(rows):
        for j in range(cols):
            if ori_k[i][j]:
                ct = ori_k[i][j]
                ni, nj = i + t, j + t  # 칸이 양 사방으로 확장된다
                spread[ct + 1].add((ni, nj))
                if ct * 2 <= t:
                    die[ct * 2] += 1
                alive += 1

    for i in range(rows):
        ori_k[i].extendleft([0] * t)
        ori_k[i].extend([0] * t)

    mod_cols = cols + t * 2
    for _ in range(t):
        ori_k.appendleft(deque([0] * mod_cols))
        ori_k.append(deque([0] * mod_cols))


def operate():
    global alive
    new_cell = set()
    for ct in range(1, t + 1):
        cur_spread = list(spread.get(ct, set()))
        new_cell.clear()
        for cx, cy in cur_spread:
            cn = ori_k[cx][cy]
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if ori_k[nx][ny] == 0:  # 빈 칸인 경우
                    ori_k[nx][ny] = cn
                    new_cell.add((nx, ny))
                    alive += 1
                elif (nx, ny) in new_cell:  # 비어있지 않고, 새로 누군가 이번에 들어온 경우
                    ori_k[nx][ny] = max(ori_k[nx][ny], cn)
        for cx, cy in list(new_cell):
            spread_t = ct + ori_k[cx][cy] + 1
            die_t = ct + ori_k[cx][cy] * 2

            if spread_t <= t:
                spread[spread_t].add((cx, cy))
            if die_t <= t:
                die[die_t] += 1
    return alive - sum(die[:t + 1])


res = []
for w in range(1, tc + 1):
    initialize()
    res.append(f'#{w} {operate()}')
print(*res, sep='\n')