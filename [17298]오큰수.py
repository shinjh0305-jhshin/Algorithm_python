import sys
input = sys.stdin.readline
stack = []
sz = int(input())
rawdata = list(map(int, input().split()))
result = [0] * sz

for idx in range(sz):
    num = rawdata[idx]
    while stack and stack[-1][1] < num:
        result[stack[-1][0]] = num
        stack.pop()
    stack.append((idx, num))

while stack:
    result[stack[-1][0]] = -1
    stack.pop()

print(*result)