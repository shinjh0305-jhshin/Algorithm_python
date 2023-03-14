import sys
Input = sys.stdin.readline
tc = int(Input())
s, e, cvs, visited = [], [], [], []
sz_cvs = 0


def find_route(x, y):
    if abs(x - e[0]) + abs(y - e[1]) <= 1000:
        return True
    for i in range(sz_cvs):
        if not visited[i]:
            d = abs(x - cvs[i][0]) + abs(y - cvs[i][1])
            if d <= 1000:
                visited[i] = True
                if find_route(cvs[i][0], cvs[i][1]):
                    return True
    return False


def operate():
    global s, e, cvs, sz_cvs, visited
    sz_cvs = int(Input())
    s = list(map(int, Input().split()))
    cvs = [list(map(int, Input().split())) for _ in range(sz_cvs)]
    e = list(map(int, Input().split()))
    visited = [False] * sz_cvs

    if find_route(s[0], s[1]):
        print("happy")
    else:
        print("sad")


for _ in range(tc):
    operate()
