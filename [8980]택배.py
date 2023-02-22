import sys
Input = sys.stdin.readline
nodes, trucks = map(int, Input().split())
sz = int(Input())
k = []
delivery = [0] * (nodes + 1)  # 해당 도시로 배달할 물건의 무게


def initialize():
    for _ in range(sz):
        k.append(tuple(map(int, Input().split())))
    for i in range(1, nodes + 1):
        k.sort(key=lambda x: x[1])


def operate():
    ans = 0
    for x, y, c in k:
        occupied = 0
        for i in range(x, y):
            occupied = max(occupied, delivery[i])  # 해당 구간에서 현재까지 가장 무거운 무게를 구한다
        avail = min(c, trucks - occupied)  # 택배와 트럭의 남는 무게 중 더 작은 값을 구한다
        ans += avail
        for i in range(x, y):
            delivery[i] += avail
    print(ans)


initialize()
operate()
