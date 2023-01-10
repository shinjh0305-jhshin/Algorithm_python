import sys
input = sys.stdin.readline
sz = int(input())
target = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()

left = 0
right = sz - 1
ans = 0;

while left < right:
    sum = ingredients[left] + ingredients[right]

    if sum == target:
        ans += 1

    if sum <= target:
        left += 1
    else:
        right -= 1

print(ans)