import sys
Input = sys.stdin.readline
sz = int(Input())


def operate():
    ans = 0
    wall = [[False] * 101 for _ in range(101)]
    for _ in range(sz):
        sx, sy = map(int, Input().split())
        for i in range(sx, sx + 10):
            for j in range(sy, sy + 10):
                if not wall[i][j]:
                    wall[i][j] = True
                    ans += 1
    print(ans)


operate()