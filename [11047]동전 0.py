import sys
Input = sys.stdin.readline
coins, target = map(int, Input().split())
coin = []
ans = 0
for _ in range(coins):
    coin.append(int(Input()))
for i in reversed(coin):
    if target >= i:
        ans += int(target / i)
        target = target % i
print(ans)