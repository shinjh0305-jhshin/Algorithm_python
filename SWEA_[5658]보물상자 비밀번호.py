from collections import deque
tc = int(input())
len_str, target, len_num = 0, 0, 0  # len_num : 숫자 1개당 길이
num = set()
qu = deque()


def initialize():
    global len_str, target, len_num, num, qu
    len_str, target = map(int, input().split())
    len_num = len_str // 4
    qu = deque(list(input().rstrip()))

    num.clear()
    split_num()


def split_num():
    list_qu = list(qu)
    for i in range(0, len_str, len_num):
        num.add(''.join(list_qu[i:i + len_num]))


def operate(tc_num):
    for _ in range(len_num):
        qu.rotate(1)
        split_num()

    res = list(num)
    res.sort(key=lambda x: int(x, 16), reverse=True)
    print(f'#{tc_num} {int(res[target - 1], 16)}')


for t in range(1, tc + 1):
    initialize()
    operate(t)
