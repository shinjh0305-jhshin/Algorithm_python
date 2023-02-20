import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
tc = int(Input())


def operate():
    books, students = map(int, Input().split())
    k = [tuple(map(int, Input().split())) for _ in range(students)]
    pq = []

    k.sort()
    s_idx = 0
    ans = 0
    for b in range(1, books + 1):
        while s_idx < students and k[s_idx][0] <= b:  # 현재 책이 시작 범위에 있는 친구들 전부 넣는다
            heappush(pq, k[s_idx][1])
            s_idx += 1
        while pq and pq[0] < b:  # 현재 책이 종료 범위에서 벗어난 친구들 전부 뺀다
            heappop(pq)
        if pq:
            heappop(pq)
            ans += 1
    print(ans)


for _ in range(tc):
    operate()
