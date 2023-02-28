from collections import deque
sz = int(input())
k = list(map(int, input().split()))
ans = 0


def dfs(cursum, idx=1):
    if idx == sz - 1:
        if cursum == k[sz - 1]:
            global ans
            ans += 1
        return
    if 0 <= cursum + k[idx] <= 20:
        dfs(cursum + k[idx], idx + 1)
    if 0 <= cursum - k[idx] <= 20:
        dfs(cursum - k[idx], idx + 1)


def operate():
    cnt = [0] * 21
    cnt[k[0]] = 1
    for j in range(1, sz - 1):
        n_cnt = [0] * 21
        for i in range(0, 21):
            if cnt[i]:
                if 0 <= i + k[j] <= 20:
                    n_cnt[i + k[j]] += cnt[i]
                if 0 <= i - k[j] <= 20:
                    n_cnt[i - k[j]] += cnt[i]
        cnt = n_cnt
    print(cnt[k[sz - 1]])


operate()
