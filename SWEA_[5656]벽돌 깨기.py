from collections import deque
tc = int(input())
it, cols, rows, blocks, ans = 0, 0, 0, 0, 0
ori_k = []
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    global it, cols, rows, ori_k, blocks, ans
    it, cols, rows = map(int, input().split())
    ans = 2134567890
    ori_k.clear()
    for _ in range(rows):
        ori_k.append(list(map(int, input().split())))
    zeros = 0
    for x in ori_k:
        zeros += x.count(0)
    blocks = cols * rows - zeros


def break_block(left, turn=0, ck=ori_k):
    global ans
    if turn == it:
        ans = min(ans, left)
        return
    if not left:
        ans = 0
        return

    for j in range(cols):
        k = [x[:] for x in ck]
        cur_left = left
        qu = deque()

        for i in range(rows):  # 시작 블록 찾기
            if k[i][j]:
                qu.append([i, j, k[i][j]])
                k[i][j] = 0
                cur_left -= 1
                break

        while qu:
            cx, cy, cl = qu.popleft()
            for d in range(4):
                for i in range(1, cl):
                    nx, ny = cx + dx[d] * i, cy + dy[d] * i
                    if not (0 <= nx < rows and 0 <= ny < cols):
                        break
                    if k[nx][ny]:
                        qu.append([nx, ny, k[nx][ny]])
                        k[nx][ny] = 0
                        cur_left -= 1

        for cj in range(cols):
            for down_row in range(rows - 1, -1, -1):
                if k[down_row][cj] == 0:
                    flag = False
                    for up_row in range(down_row - 1, -1, -1):
                        if k[up_row][cj]:
                            k[down_row][cj] = k[up_row][cj]
                            k[up_row][cj] = 0
                            flag = True
                            break
                    if not flag:
                        break

        break_block(cur_left, turn + 1, k)
        if ans == 0:
            return


for t in range(1, tc + 1):
    initialize()
    break_block(blocks)
    print(f'#{t} {ans}')
