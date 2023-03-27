import sys
Input = sys.stdin.readline
sz = int(Input())
k = [[[False] * (sz ** 2 + 1) for _ in range(sz)] for _1 in range(sz)]  # [a][b] 주변에 [c]가 있는가
seat = [[0] * sz for _ in range(sz)]  # 자리에 배정된 학생
blanks = [[0] * sz for _ in range(sz)]  # 주변의 빈 칸
friend = [[] for _ in range(sz ** 2 + 1)]  # 친구 목록
order = []  # 배치 순서
pq = [[] for _ in range(5)]  # 친구 i명과 인접한 좌석의 좌표 저장
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
score = [0, 1, 10, 100, 1000]


def initialize():
    for _ in range(sz ** 2):
        tmp = list(map(int, Input().split()))
        order.append(tmp[0])
        friend[tmp[0]].extend(tmp[1:])
    for i in range(sz):
        for j in range(sz):
            if i != 0:
                blanks[i][j] += 1
            if j > 0:
                blanks[i][j] += 1
            if j < sz - 1:
                blanks[i][j] += 1
            if i < sz - 1:
                blanks[i][j] += 1


def check_friend(idx):  # 자리를 검사하면서, pq를 만든다
    for i in range(sz):
        for j in range(sz):
            if not seat[i][j]:
                friends = len(list(filter(lambda x: k[i][j][x], friend[idx])))
                pq[friends].append((-blanks[i][j], i, j))


def give_seat(idx):
    for i in range(4, -1, -1):
        if len(pq[i]) > 0:
            pq[i].sort()
            _, x, y = pq[i][0]

            seat[x][y] = idx
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < sz and 0 <= ny < sz:
                    k[nx][ny][idx] = True
                    blanks[nx][ny] -= 1
            break

    for i in range(5):
        pq[i].clear()


def print_score():
    ans = 0
    for i in range(sz):
        for j in range(sz):
            idx = seat[i][j]
            cnt = len(list(filter(lambda x: k[i][j][x], friend[idx])))
            ans += score[cnt]
    print(ans)


def operate():
    for idx in order:
        check_friend(idx)
        give_seat(idx)
    print_score()


initialize()
operate()
