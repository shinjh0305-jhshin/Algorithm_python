import sys
Input = sys.stdin.readline
sz = int(Input())
k = [0] + [int(Input()) for _ in range(sz)]
visited, curVisited = [False] * (sz + 1), [False] * (sz + 1)
loop_start = -1
ans = []


def dfs(n):
    global loop_start
    visited[n] = curVisited[n] = True
    nn = k[n]

    if visited[nn]:  # 이미 방문한 경우
        if curVisited[nn]:  # 이번 순회에서 방문한 노드일 경우
            loop_start = nn  # 거기가 루프의 시작점이다
            curVisited[n] = False  # 초기화
            return True
    else:
        res = dfs(nn)
        curVisited[n] = False
        if res:  # 루프 내부에 있다고 보고된 경우
            ans.append(nn)  # 내 다음 숫자를 넣어준다
            if loop_start == nn:  # 루프를 빠져 나온 경우
                return False
            return True  # 아직 루프 안에 있는 경우

    curVisited[n] = False  # 초기화
    return False


def operate():
    for i in range(1, sz + 1):
        if not visited[i]:
            if dfs(i):
                ans.append(i)
    print(len(ans))
    ans.sort()
    print(*ans, sep='\n')


operate()