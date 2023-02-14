import sys
from itertools import combinations
Input = sys.stdin.readline
words, letters = map(int, Input().split())
word = []
template = 0
must_teach = 'antic'
to_teach = []


def initialize():
    global template, to_teach
    for _ in range(words):
        tmp = Input().rstrip()
        ans = 0
        for x in tmp:
            num = 1 << (ord(x) - ord('a'))
            if not ans & num:
                ans |= num
        word.append(ans)

    for x in must_teach:
        template |= 1 << (ord(x) - ord('a'))
    tmp = 'bdefghjklmopqrsuvwxyz'
    to_teach = list(tmp)


def operate():
    global template
    if letters < 5:
        print(0)
        return

    initialize()
    saved = template
    ans = 0
    for tmp in combinations(to_teach, letters - 5):
        tmp_ans = 0
        for x in tmp:
            template |= 1 << (ord(x) - ord('a'))
        for x in word:
            if x & template >= x:
                tmp_ans += 1
        ans = max(ans, tmp_ans)
        template = saved
    print(ans)


operate()