sz = int(input())
ans = [0] * sz
k = []


def initialize():
    tmp = list(input().rstrip())
    idx = 0
    for l in range(sz, 0, -1):
        arr = ['0'] * (sz - l) + tmp[idx:idx + l]
        k.append(arr)
        idx += l


def check_valid(right):
    tmp_sum = ans[right]
    for left in range(right - 1, -1, -1):
        tmp_sum += ans[left]
        if (k[left][right] == '+' and tmp_sum > 0) or (k[left][right] == '-' and tmp_sum < 0) or\
                (k[left][right] == '0' and tmp_sum == 0):
            continue
        else:
            return False
    return True


def evaluate(idx=0):
    if idx == sz:
        return True
    if k[idx][idx] == '-':
        ans[idx] = inc = -1
    elif k[idx][idx] == '+':
        ans[idx] = inc = 1
    else:
        inc = 0

    while -10 <= ans[idx] <= 10:
        if check_valid(idx):
            res = evaluate(idx + 1)  # 다음 숫자 찾아나선다
            if res:
                return True
        if inc == 0:  # 0인 경우에는 바로 리턴
            return False
        ans[idx] += inc

    return False


initialize()
evaluate()
print(*ans)
