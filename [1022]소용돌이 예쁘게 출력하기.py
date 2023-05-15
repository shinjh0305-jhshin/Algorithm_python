data = list(map(int, input().split()))
sz = max(list(map(abs, data)))
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


def operate():
    x, y = 0, 0
    num = 1  # 현재 k에 적어야 할 번호
    mov = 1  # 현재 방향으로 가야할 칸 수
    left_mov = 1  # 현재 방향으로 가야할 남은 칸 수
    cd = 0
    ans = [[0] * (data[3] - data[1] + 1) for _ in range(data[2] - data[0] + 1)]

    while True:
        if data[0] <= x <= data[2] and data[1] <= y <= data[3]:
            ans[x - data[0]][y - data[1]] = num
        num += 1

        if x == sz and y == sz:
            break

        if not left_mov:
            if cd % 2:
                mov += 1
            left_mov = mov
            cd = (cd + 1) % 4

        x, y = x + dx[cd], y + dy[cd]
        left_mov -= 1

    print_ans(ans)


def print_ans(ans):
    max_num = 0
    for i in range(len(ans)):
        max_num = max(max_num, max(ans[i]))

    len_max_num = len(str(max_num))
    res = ""

    for i in range(len(ans)):
        for num in ans[i]:
            num_st = str(num)
            if len_max_num > len(num_st):
                res += ' ' * (len_max_num - len(num_st))
            res += num_st + ' '
        if i != len(ans) - 1:
            res += '\n'
    print(res)


operate()
