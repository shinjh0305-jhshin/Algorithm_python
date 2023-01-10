import sys

input = sys.stdin.readline
total, block = map(int, input().split())
string = input().rstrip()
A, C, G, T = list(map(int, input().split()))  # A C G T

ans = 0
bases = {"A": 0, "T": 0, "G": 0, "C": 0}

initial = string[:block]
for base in initial:
    bases[base] += 1

start = 0
while True:
    if bases["A"] >= A and bases["T"] >= T and bases["G"] >= G and bases["C"] >= C:
        ans += 1
    if start == total - block:
        break
    bases[string[start]] -= 1
    bases[string[start + block]] += 1
    start += 1

print(ans)