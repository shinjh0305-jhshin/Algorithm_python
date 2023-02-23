sz = int(input())
dp = [0] * (sz + 1)


def operate():
    if sz % 2:
        print(0)
        return
    dp[2] = 3
    for i in range(4, sz + 1, 2):
        dp[i] = dp[i - 2] * 3  # 이상한 모양 없는 버전
        for j in range(i - 4, -1, -2):  # 이상한 모양이 끝에서부터 4, 6, 8, 10 ... 칸을 차지하는 경우를 센다
            dp[i] += dp[j] * 2
        dp[i] += 2  # 싹 다 이상한 모양
    print(dp[sz])


operate()
