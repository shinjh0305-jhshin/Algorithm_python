import sys
Input = sys.stdin.readline

n, m = map(int, Input().split())
rawdata = set([Input() for _ in range(n)])
cnt = 0

for _ in range(m):
    target = Input()
    if target in rawdata:
        cnt += 1

print(cnt)