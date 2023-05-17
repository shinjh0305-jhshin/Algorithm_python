import sys
from heapq import heappush, heappop
Input = sys.stdin.readline
tc = int(Input())
nodes, edges, hacked = 0, 0, 0
k = []  # computer, time


def initialize():
    global nodes, edges, hacked, k
    nodes, edges, hacked = map(int, Input().split())
    k = [[] for _ in range(nodes + 1)]
    for _ in range(edges):
        a, b, s = map(int, Input().split())
        k[b].append([a, s])


def operate():
    pq = []
    hack_time = [sys.maxsize] * (nodes + 1)
    heappush(pq, [0, hacked])  # time, computer
    hack_time[hacked] = 0
    hacked_cpu = 0
    last_hack_time = 0

    while pq:
        ct, cc = heappop(pq)
        if hack_time[cc] < ct:
            continue
        hacked_cpu += 1
        last_hack_time = max(last_hack_time, ct)
        for nc, tt in k[cc]:
            nt = ct + tt
            if hack_time[nc] > nt:
                hack_time[nc] = nt
                heappush(pq, [nt, nc])
    print(hacked_cpu, last_hack_time)


for _ in range(tc):
    initialize()
    operate()
