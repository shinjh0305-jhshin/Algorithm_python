import sys
sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
k = [list(map(int, Input().split())) for _ in range(10)]
left_paper = [5] * 6
ans = sys.maxsize


def check_avail(i, j, sz):
    if i + sz > 10 or j + sz > 10:
        return False
    for x in range(i, i + sz):
        for y in range(j, j + sz):
            if not k[x][y]:
                return False
    return True


def toggle(i, j, sz):
    for x in range(i, i + sz):
        for y in range(j, j + sz):
            k[x][y] = int(not k[x][y])


def dfs(i=0, j=0, d=0):
    s = j
    for x in range(i, 10):
        for y in range(s, 10):
            if k[x][y]:
                for z in range(1, 6):
                    if not left_paper[z]:
                        continue
                    if check_avail(x, y, z):
                        toggle(x, y, z)
                        left_paper[z] -= 1

                        dfs(x, y + z, d + 1)

                        toggle(x, y, z)
                        left_paper[z] += 1
                    else:
                        break
                return
        s = 0
    global ans
    ans = min(ans, d)


def operate():
    dfs()
    print(-1) if ans == sys.maxsize else print(ans)


operate()
