s1 = input()
s2 = input()
len_s1 = len(s1)
len_s2 = len(s2)
dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]


def find_lcs_length():
    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    print(dp[len_s1][len_s2])


def get_lcs():
    res = [''] * dp[len_s1][len_s2]
    x = len_s1
    y = len_s2
    res_idx = 0
    while x > 0 and y > 0:
        if s1[x - 1] == s2[y - 1]:
            res[res_idx] = s1[x - 1]
            res_idx += 1
            x -= 1
            y -= 1
        else:
            if dp[x][y] == dp[x][y - 1]:
                y -= 1
            else:
                x -= 1
    res.reverse()
    print(*res, sep='')


find_lcs_length()
get_lcs()
