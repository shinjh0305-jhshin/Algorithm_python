import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
k = [list(map(int, Input().split())) for _ in range(rows)]
dp_left = [[-sys.maxsize] * cols for _ in range(rows)]
dp_right = [[-sys.maxsize] * cols for _ in range(rows)]
ans = [[0] * cols for _ in range(rows)]


def operate():
    for i in range(cols):
        ans[0][i] = sum(k[0][:i + 1])

    for i in range(1, rows):
        # dp_left
        dp_left[i][0] = ans[i - 1][0] + k[i][0]
        for j in range(1, cols):
            dp_left[i][j] = max(ans[i - 1][j], dp_left[i][j - 1]) + k[i][j]
        # dp_right
        dp_right[i][cols - 1] = ans[i - 1][cols - 1] + k[i][cols - 1]
        for j in range(cols - 2, -1, -1):
            dp_right[i][j] = max(ans[i - 1][j], dp_right[i][j + 1]) + k[i][j]
        for j in range(cols):
            ans[i][j] = max(dp_left[i][j], dp_right[i][j])

    print(ans[rows - 1][cols - 1])


operate()