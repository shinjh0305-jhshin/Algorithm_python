from bisect import bisect_left  # 이분탐색을 위한 라이브러리
sz = int(input())
k = list(map(int, input().split()))
queries = int(input())
query = list(map(int, input().split()))


def operate():
    k.sort()

    ans = []
    for q in query:
        if q > k[-1] or k[bisect_left(k, q)] != q:  # k에 있는 수보다 크거나, 포함하지 않는 경우
            ans.append(0)
        else:
            ans.append(1)
    print(*ans, sep='\n')


operate()
