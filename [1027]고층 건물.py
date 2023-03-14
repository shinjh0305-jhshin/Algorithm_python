import sys
Input = sys.stdin.readline
sz = int(Input())
k = list(map(int, Input().split()))


def operate():
    ans = 0
    for i in range(sz):
        h_i = k[i]
        cur_ans = 0
        cur_slope = sys.maxsize
        for mov in range(i - 1, -1, -1):
            h_mov = k[mov]
            test_slope = (h_mov - h_i) / (mov - i)
            if test_slope < cur_slope:
                cur_slope = test_slope
                cur_ans += 1
        cur_slope = -sys.maxsize
        for mov in range(i + 1, sz):
            h_mov = k[mov]
            test_slope = (h_mov - h_i) / (mov - i)
            if test_slope > cur_slope:
                cur_slope = test_slope
                cur_ans += 1
        ans = max(cur_ans, ans)
    print(ans)


operate()