import sys
Input = sys.stdin.readline
sz = int(Input())
k = [Input().rstrip() for _ in range(sz)]
res = [2] * sz


def find_palindrome(l, r, idx, status=0):
    while l <= r:
        if k[idx][l] == k[idx][r]:
            l += 1
            r -= 1
        elif status == 0:
            if k[idx][l + 1] == k[idx][r]:
                find_palindrome(l + 1, r, idx, 1)
            if k[idx][l] == k[idx][r - 1]:
                find_palindrome(l, r - 1, idx, 1)
            return
        else:
            return
    res[idx] = status


def operate():
    for i in range(sz):
        find_palindrome(0, len(k[i]) - 1, i)

    print(*res, sep='\n')


operate()
