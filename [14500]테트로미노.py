import sys
Input = sys.stdin.readline
rows, cols = map(int, Input().split())
graph = [list(map(int, Input().split())) for _ in range(rows)]


def make_row_3(cx, cy):  # 가로로 세 블럭 나란히
    ans = -sys.maxsize
    d = [(-1, 0), (-1, 1), (-1, 2), (0, 3), (1, 0), (1, 1), (1, 2)]

    row_sum = graph[cx][cy] + graph[cx][cy + 1] + graph[cx][cy + 2]
    for dx, dy in d:
        nx = cx + dx
        ny = cy + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            ans = max(ans, row_sum + graph[nx][ny])

    return ans


def make_col_3(cx, cy):  # 세로로 세 블럭 나란히
    ans = -sys.maxsize
    d = [(0, -1), (1, -1), (2, -1), (3, 0), (0, 1), (1, 1), (2, 1)]

    col_sum = graph[cx][cy] + graph[cx + 1][cy] + graph[cx + 2][cy]
    for dx, dy in d:
        nx = cx + dx
        ny = cy + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            ans = max(ans, col_sum + graph[nx][ny])

    return ans


def make_2(cx, cy):  # 가로로 두 블럭 나란히
    ans = -sys.maxsize
    row_sum = graph[cx][cy] + graph[cx][cy + 1]
    d = [[(-1, 0), (-1, -1)], [(-1, 0), (-1, 1)], [(-1, 1), (-1, 2)],
         [(-1, 1), (1, 0)], [(-1, 0), (1, 1)]]

    for k in d:
        nx1 = cx + k[0][0]
        nx2 = cx + k[1][0]
        ny1 = cy + k[0][1]
        ny2 = cy + k[1][1]
        if 0 <= nx1 < rows and 0 <= nx2 < rows and 0 <= ny1 < cols and 0 <= ny2 < cols:
            ans = max(ans, row_sum + graph[nx1][ny1] + graph[nx2][ny2])

    return ans


def operate():
    ans = -sys.maxsize
    for i in range(rows):
        for j in range(cols):
            if j <= cols - 3:
                ans = max(ans, make_row_3(i, j))
            if i <= rows - 3:
                ans = max(ans, make_col_3(i, j))
            if j <= cols - 2:
                ans = max(ans, make_2(i, j))
    print(ans)

operate()
