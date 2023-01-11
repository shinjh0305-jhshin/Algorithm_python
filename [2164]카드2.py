from collections import deque
sz = int(input())
qu = deque()

for i in range(1, sz + 1):
    qu.append(i)

while len(qu) > 1:
    qu.popleft()
    qu.append(qu.popleft())

print(qu[0])