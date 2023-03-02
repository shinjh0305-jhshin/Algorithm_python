import sys
from collections import deque
Input = sys.stdin.readline
sz = int(Input())
k = list(map(int, Input().split()))


def operate():
    k.reverse()  # 맨 뒤부터 넣기 위해 뒤집는다
    ans = []  # 정답을 저장하는 리스트
    st = deque()  # 스택
    for x in k:
        while st and st[-1] <= x:
            st.pop()
        ans.append(-1) if not st else ans.append(st[-1])
        st.append(x)
    ans.reverse()
    print(*ans)


operate()
