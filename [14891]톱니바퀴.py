from collections import deque
gear = [deque(list(map(int, input()))) for _ in range(4)]


def rotate(x, d):
    if d == 1:  # clockwise
        tmp = gear[x].pop()
        gear[x].appendleft(tmp)
    else:  # anti-clockwise
        tmp = gear[x].popleft()
        gear[x].append(tmp)


def operate():
    sz = int(input())
    for _ in range(sz):
        x, d = map(int, input().split())  # d : 시계(1), 반시계(-1)
        x -= 1  # 0번부터 시작
        qu = deque()  # 번호, 탐색방향(-1 : 왼쪽, 1 : 오른쪽), 시계/반시계
        if x > 0 and gear[x][6] != gear[x - 1][2]:
            qu.append((x - 1, -1, -d))
        if x < 3 and gear[x][2] != gear[x + 1][6]:
            qu.append((x + 1, 1, -d))
        rotate(x, d)

        while qu:
            x, d, r = qu.popleft()
            if d == -1 and x > 0 and gear[x][6] != gear[x - 1][2]:
                qu.append((x - 1, -1, -r))
            if d == 1 and x < 3 and gear[x][2] != gear[x + 1][6]:
                qu.append((x + 1, 1, -r))
            rotate(x, r)

    ans = 0
    for i in range(4):
        ans += gear[i][0] * (1 << i)
    print(ans)


operate()
