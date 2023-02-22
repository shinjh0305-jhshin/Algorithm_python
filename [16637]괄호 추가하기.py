import sys
sys.setrecursionlimit(10 ** 6)

len_k = int(input())
k = '+' + input().rstrip()
ans = -sys.maxsize


def calc(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    else:
        return x * y


def dfs(idx=1, cur_sum=0):
    global ans
    if idx == len_k:
        ans = max(ans, calc(cur_sum, int(k[idx]), k[idx - 1]))
        return
    if idx > len_k:
        ans = max(ans, cur_sum)
        return
    # 괄호 O
    dfs(idx + 4, calc(cur_sum, calc(int(k[idx]), int(k[idx + 2]), k[idx + 1]), k[idx - 1]))
    # 괄호 X
    dfs(idx + 2, calc(cur_sum, int(k[idx]), k[idx - 1]))


def operate():
    dfs()
    print(ans)


operate()
