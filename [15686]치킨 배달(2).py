import sys
from itertools import combinations
Input = sys.stdin.readline
nodes, shops = map(int, Input().split())
shop = []
house = []


def initialize():
    for i in range(nodes):
        tmp = list(map(int, Input().split()))
        for j in range(nodes):
            if tmp[j] == 2:
                shop.append([i, j])
            elif tmp[j] == 1:
                house.append([i, j])


def operate():
    ans = sys.maxsize
    for tmp_shop in combinations(range(0, len(shop)), shops):  # tmp_shop : 남길 치킨집
        dist_to_house = [sys.maxsize] * len(house)
        for i in tmp_shop:
            sx, sy = shop[i]
            for j in range(len(house)):
                hx, hy = house[j]
                dist_to_house[j] = min(dist_to_house[j], abs(hx - sx) + abs(hy - sy))
        ans = min(ans, sum(dist_to_house))
    print(ans)


initialize()
operate()

