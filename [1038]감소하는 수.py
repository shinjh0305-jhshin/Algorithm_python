target = int(input())
dp = [[0] * 10 for _ in range(11)]


def operate():
    global target
    if 0 <= target < 10:
        print(target)
        return
    target += 1  # 우리 사정에 맞게 숫자를 조금 바꾼다.
    dp[1] = [1] * 10
    cur_sum = 10

    # dp[자릿수][MSD]를 만든다
    flag = False
    for row in range(2, 11):
        for col in range(10):
            if col < row - 1:
                continue
            dp[row][col] = dp[row][col - 1] + dp[row - 1][col - 1]
            cur_sum += dp[row][col]
            if cur_sum >= target:
                flag = True
                break
        if flag:
            break
    if not flag:
        print(-1)
        return

    # 숫자를 찾아 나선다
    ans = 0
    while row:
        ans = ans * 10 + col  # MSD 부터 하나씩 저장한다
        cur_sum -= dp[row][col]
        row -= 1
        for col in range(10):
            cur_sum += dp[row][col]
            if cur_sum >= target:
                break
    print(ans)


operate()