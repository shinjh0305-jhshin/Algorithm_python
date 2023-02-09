from collections import deque
S = input()
T = deque(list(input()))


def operate():
    len_s = len(S)
    len_t = len(T)
    is_reversed = False
    for _ in range(len_t - len_s):
        if is_reversed:
            tmp = T.popleft()
        else:
            tmp = T.pop()
        if tmp == 'B':
            is_reversed = not is_reversed
        if len(T) == len_s:
            break
    res = ''.join(T)
    if is_reversed:
        res = ''.join(reversed(res))
    if S == res:
        print(1)
    else:
        print(0)


operate()
