import sys
Input = sys.stdin.readline
sz = int(Input())
k = [list(map(int, Input().split())) for _ in range(sz)]
avail = [True] * sz
ans = 0


def dfs(pick=0):
    if pick == sz:  # 가장 오른쪽 계란
        global ans
        ans = max(ans, avail.count(False))
        return
    candidate = list(filter(lambda x: avail[x], range(0, pick))) + \
        list(filter(lambda x: avail[x], range(pick + 1, sz)))  # 깰 수 있는 계란의 index. 자기자신 제외
    if len(candidate) == 0 or not avail[pick]:  # 깰 수 있는 계란이 없거나, 깨진 계란을 집은 경우
        dfs(pick + 1)
    else:
        for ne in candidate:
            k[pick][0], k[ne][0] = k[pick][0] - k[ne][1], k[ne][0] - k[pick][1]  # 내구도 감소
            if k[pick][0] <= 0:  # 상태 업데이트
                avail[pick] = False
            if k[ne][0] <= 0:
                avail[ne] = False

            dfs(pick + 1)

            avail[pick] = avail[ne] = True  # 상태 복원
            k[pick][0], k[ne][0] = k[pick][0] + k[ne][1], k[ne][0] + k[pick][1]  # 내구도 복원


def operate():
    dfs()
    print(ans)


operate()
