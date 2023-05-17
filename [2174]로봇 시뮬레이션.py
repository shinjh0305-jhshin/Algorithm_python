import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
robots, ops = map(int, Input().split())
graph = [[0] * cols for _ in range(rows)]  # 현재 땅의 모습
cur_robot = [[] for _ in range(robots + 1)]  # robot : position
robot_dir = [0] * (robots + 1)
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def initialize():
    d_trans = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
    for i in range(1, robots + 1):
        x, y, d = Input().split()
        x, y = int(x) - 1, int(y) - 1
        graph[x][y] = i
        cur_robot[i] = [x, y]
        robot_dir[i] = d_trans[d]


def operate():
    for _ in range(ops):
        robot, op, it = Input().split()
        robot, it = int(robot), int(it)
        cd = robot_dir[robot]

        if op == 'L':
            nd = (cd - it) % 4
            robot_dir[robot] = nd
        elif op == 'R':
            nd = (cd + it) % 4
            robot_dir[robot] = nd
        else:
            cx, cy = cur_robot[robot]
            graph[cx][cy] = 0
            for i in range(it):
                cx, cy = cx + dx[cd], cy + dy[cd]
                if not (0 <= cx < rows and 0 <= cy < cols):
                    print(f'Robot {robot} crashes into the wall')
                    return
                if graph[cx][cy] != 0:
                    print(f'Robot {robot} crashes into robot {graph[cx][cy]}')
                    return
            graph[cx][cy] = robot
            cur_robot[robot] = [cx, cy]
    print("OK")


initialize()
operate()
