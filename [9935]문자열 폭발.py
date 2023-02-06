k = input().rstrip()
t = input().rstrip()
stack = []
length = len(t)
ends = t[-1]


def operate():
    for x in k:
        stack.append(x)
        if x == ends and ''.join(stack[-length:]) == t:
            del stack[-length:]
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')


operate()
