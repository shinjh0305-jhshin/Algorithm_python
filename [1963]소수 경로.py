import sys
from collections import deque
Input = sys.stdin.readline
tc = int(Input())
isPrime = [True] * 10001


def sieve():
    isPrime[1] = False
    for i in range(2, 100):
        if isPrime[i]:
            num = i * 2
            while num <= 10000:
                isPrime[num] = False
                num += i


def operate():
    a, b = map(int, Input().split())
    visited = [False] * 10001
    qu = deque()

    visited[a] = True
    qu.append(a)

    ans = 0
    while qu:
        len_qu = len(qu)
        for _ in range(len_qu):
            cn = qu.popleft()  # 현재 숫자
            if cn == b:
                print(ans)
                return
            x = list(map(int, str(cn)))  # 현재 숫자 각 자릿수 뽑아내기
            for i in range(4):
                td = x[i]  # 현재 숫자 현재 자릿수 임시 저장
                for nd in range(x[i] + 1, 10):
                    x[i] = nd
                    nn = int(''.join(map(str, x)))
                    if nn < 10000 and not visited[nn] and isPrime[nn]:  # 10000 까지 확인
                        visited[nn] = True
                        qu.append(nn)
                x[i] = td  # 자릿수 복원
                for nd in range(x[i] - 1, -1, -1):
                    x[i] = nd
                    nn = int(''.join(map(str, x)))
                    if nn >= 1000 and not visited[nn] and isPrime[nn]:  # 1000까지 확인
                        visited[nn] = True
                        qu.append(nn)
                x[i] = td  # 자릿수 복원
        ans += 1
    print("Impossible")


sieve()
for _ in range(tc):
    operate()
