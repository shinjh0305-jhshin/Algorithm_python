import sys
input = sys.stdin.readline
nums = int(input())

stack = []
answer = ""
nextNum = 1
isPossible = True

for i in range(nums):
    curNum = int(input())

    while curNum >= nextNum:
        stack.append(nextNum)
        answer += "+\n"
        nextNum += 1

    if curNum == stack[-1]:
        answer += "-\n"
        stack.pop()
    else:
        isPossible = False
        break

if isPossible:
    print(answer)
else:
    print("NO")