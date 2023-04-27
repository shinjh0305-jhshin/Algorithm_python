import sys
from collections import deque, defaultdict
Input = sys.stdin.readline
sz = int(Input())
need = [defaultdict(int) for _ in range(sz + 1)]  # 필요한 부품의 개수
prev_nodes = [0] * (sz + 1)  # 자신이 조립되기 위해서 필요한 부품의 종류 수
consists = [[] for _ in range(sz + 1)]  # 자신이 조립되기 위해서 필요한 부품의 종류과 개수
k = [[] for _ in range(sz + 1)]  # 자신을 지으면 누구가 지어질 수 있는지
qu = deque()  # 지어질 수 있는 부품들


def initialize():
    it = int(Input())
    for _ in range(it):
        x, y, w = map(int, Input().split())
        prev_nodes[x] += 1
        consists[x].append([y, w])
        k[y].append(x)
    for i in range(1, sz + 1):
        if prev_nodes[i] == 0:
            need[i][i] = 1
            qu.append(i)


def operate():
    while True:
        cn = qu.popleft()
        for nn in k[cn]:
            prev_nodes[nn] -= 1
            if prev_nodes[nn] == 0:
                qu.append(nn)
                for part, qty in consists[nn]:
                    for sub_part, sub_qty in need[part].items():
                        need[nn][sub_part] += sub_qty * qty
                if nn == sz:
                    for x, y in sorted(need[sz].items()):
                        print(x, y)
                    return


initialize()
operate()
