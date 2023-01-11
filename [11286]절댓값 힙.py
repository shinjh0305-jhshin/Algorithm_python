import sys
import heapq
input = sys.stdin.readline
heap = []
sz = int(input())
for i in range(sz):
    num = int(input())
    if num:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
