import sys
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]
mov = {0.01: [(1, 0, 0), (0, 0, 1)], 0.02: [(2, 1, 0), (0, 1, 2)],
       0.07: [(1, 1, 0), (0, 1, 1)], 0.10: [(1, 2, 0), (0, 2, 1)], 0.05: [(0, 3, 0)]}
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
ans = 0


def mov_tornado(cx, cy, cd):
    global ans
    tx, ty = cx + dx[cd], cy + dy[cd]
    left_sand = k[tx][ty]
    for percent, d in mov.items():
        mov_sand = int(k[tx][ty] * percent)
        for prev, cur, after in d:
            dcx, dcy = dx[(cd - 1) % 4] * prev + dx[cd] * cur + dx[(cd + 1) % 4] * after, \
                dy[(cd - 1) % 4] * prev + dy[cd] * cur + dy[(cd + 1) % 4] * after
            nx, ny = cx + dcx, cy + dcy
            if 0 <= nx < sz and 0 <= ny < sz:
                k[nx][ny] += mov_sand  # move sand
            else:
                ans += mov_sand  # sand out of range
            left_sand -= mov_sand
    nx, ny = cx + dx[cd] * 2, cy + dy[cd] * 2
    if 0 <= nx < sz and 0 <= ny < sz:
        k[nx][ny] += left_sand
    else:
        ans += left_sand
    k[tx][ty] = 0


def operate():
    cx, cy, cd = sz // 2, sz // 2, 1
    for d in range(1, sz + 1):
        for it in range(2):
            for _ in range(d):
                mov_tornado(cx, cy, cd)
                cx, cy = cx + dx[cd], cy + dy[cd]
            cd = (cd + 1) % 4
            if d == sz:
                break
    print(ans)

operate()
