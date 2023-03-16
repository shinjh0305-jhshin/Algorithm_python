import sys
Input = sys.stdin.readline
sz, trees, years = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(sz)]
nutrient = [[5] * sz for _ in range(sz)]
tree = [[[] for _ in range(sz)] for _1 in range(sz)]


def spring_summer():
    for i in range(sz):
        for j in range(sz):
            if len(tree) > 1:
                tree[i][j].sort()
            for m in range(len(tree[i][j])):  # 나무들 순회
                ct = tree[i][j][m]
                if nutrient[i][j] >= ct:
                    tree[i][j][m] += 1
                    nutrient[i][j] -= ct
                else:
                    for n in range(m, len(tree[i][j])):  # 죽는 나무들 순회
                        nutrient[i][j] += tree[i][j][n] // 2
                    del tree[i][j][m:]
                    break


def autumn():
    global tree
    new_tree = [[[] for _ in range(sz)] for _1 in range(sz)]
    dx, dy = [1, 0, -1, -1, -1, 0, 1, 1], [-1, -1, -1, 0, 1, 1, 1, 0]

    for i in range(sz):
        for j in range(sz):
            for t in tree[i][j]:
                new_tree[i][j].append(t)
                if t % 5 == 0:
                    for x in range(8):
                        nx, ny = i + dx[x], j + dy[x]
                        if 0 <= nx < sz and 0 <= ny < sz:
                            new_tree[nx][ny].append(1)
    tree = new_tree


def winter():
    for i in range(sz):
        for j in range(sz):
            nutrient[i][j] += k[i][j]


def operate():
    for _ in range(trees):
        x, y, yr = map(int, Input().split())
        tree[x - 1][y - 1].append(yr)

    for _ in range(years):
        spring_summer()
        autumn()
        winter()

    ans = 0
    for i in range(sz):
        for j in range(sz):
            ans += len(tree[i][j])

    print(ans)


operate()

