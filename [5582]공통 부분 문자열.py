A = input().rstrip()
B = input().rstrip()
len_a = len(A)
len_b = len(B)
dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]


def operate():
    ans = 0
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                ans = max(ans, dp[i][j])

    print(ans)


operate()