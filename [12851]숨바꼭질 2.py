from collections import deque
su, sis = map(int, input().split())
dp = [0] * 100005
visited = [0] * 100005


def operate():
    if su == sis:
        return [0, 1]
    dp[su] = 1
    qu = deque()
    qu.append(su)

    t = 1
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cn = qu.popleft()
            nns = [cn - 1, cn + 1, cn * 2]
            for nn in nns:
                if not (0 <= nn <= 100000):
                    continue
                if not visited[nn]:
                    visited[nn] = t
                    dp[nn] = dp[cn]
                    qu.append(nn)
                elif visited[nn] == t:
                    dp[nn] += dp[cn]
        if visited[sis]:
            return [t, dp[sis]]
        t += 1


print(*operate(), sep='\n')
