import sys
from collections import deque
Input = sys.stdin.readline
tc = int(Input())


def operate():
    operations = Input().rstrip()
    sz = int(Input())
    if sz == 0:
        qu = deque()
        Input()
    else:
        qu = deque(Input().rstrip()[1:-1].split(','))
    pop_left = True  # 왼쪽에서 pop 할지를 나타낸다
    for op in operations:
        if op == 'R':
            pop_left = not pop_left
        else:
            if len(qu) == 0:
                print('error')
                return
            if pop_left:
                qu.popleft()
            else:
                qu.pop()
    if not pop_left:
        qu.reverse()
    ans = '[' + ','.join(qu) + ']'
    print(ans)


for _ in range(tc):
    operate()
