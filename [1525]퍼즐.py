from collections import deque
visited = set()
target = [{3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5}, {1, 2, 4, 5, 7, 8}, {0, 1, 3, 4, 6, 7}]
d = [-3, 3, -1, 1]


def bfs(tmp):
    ans = 1
    qu = deque([tmp])
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cn = qu.popleft()
            idx = cn.index('0')
            nn = list(cn)

            for i in range(4):
                if idx in target[i]:
                    nn[idx + d[i]], nn[idx] = nn[idx], nn[idx + d[i]]
                    tmp = ''.join(nn)
                    if tmp == '123456780':
                        return ans
                    if tmp not in visited:
                        qu.append(tmp)
                        visited.add(tmp)
                    nn[idx + d[i]], nn[idx] = nn[idx], nn[idx + d[i]]

        ans += 1

    return -1


def operate():
    tmp = ''
    for i in range(3):
        tmp += ''.join(list(input().split()))

    if tmp == '123456780':
        print(0)
        return

    visited.add(tmp)
    print(bfs(tmp))


operate()
