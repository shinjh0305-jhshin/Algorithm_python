from heapq import heappop, heappush
subin, sister = map(int, input().split())
visited = [False] * 100001
pq = []


def operate():
    heappush(pq, (0, subin))

    while True:
        t, x = heappop(pq)
        if x == sister:
            print(t)
            return
        if visited[x]:
            continue

        visited[x] = True
        if x - 1 >= 0 and not visited[x - 1]:
            heappush(pq, (t + 1, x - 1))
        if x + 1 <= 100000 and not visited[x + 1]:
            heappush(pq, (t + 1, x + 1))
        if x * 2 <= 100000 and not visited[x * 2]:
            heappush(pq, (t, x * 2))


operate()