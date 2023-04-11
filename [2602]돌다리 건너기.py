from collections import defaultdict
seq = input().rstrip()
bridge = [input().rstrip() for _ in range(2)]
len_seq, len_br = len(seq), len(bridge[0])
dp = [[[0] * len_seq for _ in range(len_br)] for _ in range(2)]  # 다리 종류, 다리에서 index, seq에서 index


def initialize():
    last_chr = seq[-1]
    for i in range(len_br):
        for x in range(2):
            if bridge[x][i] == last_chr:
                dp[x][i][len_seq - 1] += 1


def operate():
    for i in range(len_seq - 2, -1, -1):  # seq를 뒤에서부터 한 글자씩 떼어온다
        cur_chr, next_chr = seq[i], seq[i + 1]  # 현재 돌다리, 다음 돌다리
        acc = [0, 0]  # 다음 돌다리로 넘어갈 수 있는 경우의 수
        for j in range(len_br - 1, -1, -1):  # bridge를 뒤에서부터 읽어온다
            for br_idx in range(2):  # 두 개의 bridge에 대해
                if bridge[br_idx][j] == cur_chr:  # 현재 돌다리가 될 수 있는 경우
                    dp[br_idx][j][i] += acc[(br_idx + 1) % 2]
            for br_idx in range(2):  # 두 개의 bridge에 대해
                if bridge[br_idx][j] == next_chr:  # 다음 현재 돌다리의 다음 돌다리가 될 수 있는 경우
                    acc[br_idx] += dp[br_idx][j][i + 1]
    ans = 0
    for i in range(len_br):
        for x in range(2):
            if bridge[x][i] == seq[0]:
                ans += dp[x][i][0]
    print(ans)


initialize()
operate()
