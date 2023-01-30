import sys, math
from collections import deque
Input = sys.stdin.readline
sz = int(Input())
rawdata = list(map(int, Input().split()))


def find_nth_permutation(l, n):  # 숫자의 개수, n번째 숫자 구하기
    if l == 0:
        ans.append(nums[-1])
        return
    seq = math.factorial(l)
    target = math.ceil(n / seq)
    ans.append(nums.pop(target))
    find_nth_permutation(l - 1, n - seq * (target - 1))


def find_perm_idx():
    res = 1
    mov = sz - 1
    for num in rawdata[1:]:
        idx = nums.index(num)
        res += math.factorial(mov) * idx
        nums.pop(idx)
        mov -= 1
    return res


nums = [i for i in range(sz + 1)]
if rawdata[0] == 1:
    ans = []
    find_nth_permutation(sz - 1, rawdata[1])
    print(*ans)
else:
    nums.pop(0)
    print(find_perm_idx())
