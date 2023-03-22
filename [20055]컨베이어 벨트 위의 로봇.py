import sys
from collections import deque
Input = sys.stdin.readline

n, k = map(int, Input().split())
belt = deque(list(map(int, Input().split())))
robot = deque([False] * n)


def operate():
    res = 0
    while True:
        belt.rotate(1)
        robot.rotate(1)
        robot[-1] = False  # 로봇 내리기
        if True in robot:
            for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
                if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                    robot[i + 1] = 1
                    robot[i] = 0
                    belt[i + 1] -= 1
            robot[-1] = False  # 로봇 내리기
        if belt[0] >= 1:
            robot[0] = True
            belt[0] -= 1
        res += 1
        if belt.count(0) >= k:
            break
    print(res)

operate()