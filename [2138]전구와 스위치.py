import sys
sys.setrecursionlimit(10 ** 6)
sz = int(input())
ori = list(map(int, input().rstrip()))
ans = list(map(int, input().rstrip()))
to_modify = [-1, 0, 1]
res = sys.maxsize


def toggle_switch(pos):
    for d in to_modify:  # 스위치 상태 바꾼다
        if 0 <= pos + d < sz:
            ori[pos + d] = not ori[pos + d]


def dfs(idx=0, history=0):
    if idx == sz:
        if ori[sz - 1] == ans[sz - 1]:
            global res
            res = min(res, history)
        return
    if idx > 0:
        if ori[idx - 1] == ans[idx - 1]:  # 내 왼쪽의 스위치가 맞은 상태면 절대 바꾸면 안 된다
            dfs(idx + 1, history)
        else:  # 내 왼쪽의 스위치가 안맞은 상태면 무조건 바꿔야 한다
            toggle_switch(idx)
            dfs(idx + 1, history + 1)
            toggle_switch(idx)
    else:
        dfs(idx + 1, history)  # 가장 첫 스위치는 자유롭다

        toggle_switch(idx)
        dfs(idx + 1, history + 1)


def operate():
    dfs()
    print(-1) if res == sys.maxsize else print(res)


operate()
