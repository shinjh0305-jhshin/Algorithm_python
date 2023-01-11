import sys

sys.setrecursionlimit(10 ** 6)
Input = sys.stdin.readline
length = int(Input())

def isprime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == length:
        print(num)
    else:
        for i in range(1, 10, 2):
            temp = num * 10 + i
            if isprime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)