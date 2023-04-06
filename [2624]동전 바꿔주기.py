import sys
Input = sys.stdin.readline
target = int(Input())
coins = int(Input())
coin = [list(map(int, Input().split())) for _ in range(coins)]
dp = [0] * (target + 1)


def operate():
    dp[0] = 1
    for cur_coin, cur_coins in coin:
        for cur_price in range(target, cur_coin - 1, -1):
            used_coins = 1
            while used_coins <= cur_coins and cur_coin * used_coins <= cur_price:
                dp[cur_price] += dp[cur_price - cur_coin * used_coins]
                used_coins += 1
    print(dp[target])


operate()

