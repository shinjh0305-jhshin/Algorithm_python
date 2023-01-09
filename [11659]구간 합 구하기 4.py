import sys
input = sys.stdin.readline

sz, iter = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [0]

sum = 0;
for num in numbers:
    sum = sum + num
    dp.append(sum)

for i in range(iter):
    start, end = map(int, input().split())
    print(dp[end] - dp[start - 1])