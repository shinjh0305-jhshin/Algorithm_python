import copy
k = [[] for _ in range(4)]
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
ans = 0


def initialize():
    tmp = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(0, 8, 2):
            k[i].append([tmp[i][j], tmp[i][j + 1] - 1])  # fish index, dir


def move(score, next_fish=k):
    idx = [[] for _ in range(17)]  # 각 물고기가 있는 row, col, dir
    for i in range(4):
        for j in range(4):
            if next_fish[i][j]:
                idx[next_fish[i][j][0]] = [i, j, next_fish[i][j][1]]

    # 우선 물고기 움직인다
    fish = copy.deepcopy(next_fish)  # fish index, dir
    for i in range(1, 17):
        if not idx[i]:  # 상어한테 먹힌 물고기는 pass
            continue
        cx, cy, cd = idx[i]
        for _ in range(8):
            nx, ny = cx + dx[cd], cy + dy[cd]
            if 0 <= nx < 4 and 0 <= ny < 4:  # 범위 내에 있고
                if fish[nx][ny] and fish[nx][ny][0] == 0:  # 상어인 경우
                    cd = (cd + 1) % 8
                    continue
                fish[cx][cy][1] = cd  # 현재 물고기의 방향 정보 업데이트
                if fish[nx][ny]:  # 이동한 곳에 물고기가 있으면, 그 물고기의 위치 정보 업데이트
                    idx[fish[nx][ny][0]] = [cx, cy, idx[fish[nx][ny][0]][2]]
                fish[cx][cy], fish[nx][ny] = fish[nx][ny], fish[cx][cy]  # 물고기 위치 교환
                break
            cd = (cd + 1) % 8

    # 상어 움직인다
    cx, cy, cd = idx[0]  # 상어의 위치
    fish[cx][cy] = []  # 상어 있던 자리 비운다
    flag = False
    while True:
        nx, ny = cx + dx[cd], cy + dy[cd]  # 상어 위치 옮긴다
        if 0 <= nx < 4 and 0 <= ny < 4:
            if fish[nx][ny]:
                flag = True
                temp_score = score + fish[nx][ny][0]  # 상어가 먹은 물고기
                temp_fish = fish[nx][ny][:]

                fish[nx][ny] = [0, temp_fish[1]]
                move(temp_score, fish)
                fish[nx][ny] = temp_fish[:]
            cx, cy = nx, ny
        else:
            break
    if not flag:
        global ans
        ans = max(ans, score)


def operate():
    init = k[0][0][0]
    k[0][0] = [0, k[0][0][1]]
    move(init)
    print(ans)


initialize()
operate()
