import sys
Input = sys.stdin.readline
sz = int(Input())
flower = [list(map(int, Input().split())) for _ in range(sz)]
flower.sort()


def operate():
    idx = 0
    ans = 0
    start_date = [3, 1]  # 무조건 이 날에 피어 있어야 한다.

    while True:
        max_end_date = [-1, -1]
        if start_date >= [12, 1]:
            return ans
        # 이전 꽃이 진 그날에 피어있는 꽃 중에서 가장 지는 날이 늦은 꽃 찾는다.
        while idx < sz and flower[idx][0:2] <= start_date:
            end_date = flower[idx][2:]
            if start_date < end_date:
                max_end_date = max(max_end_date, end_date)
            idx += 1
        # 찾는 꽃이 없다
        if max_end_date == [-1, -1]:
            return 0
        ans += 1
        start_date = max_end_date[:]


print(operate())

