tc = int(input())
tmp = ['1']
sz = 0


def dfs(num):
    if num == sz:
        expr = ''.join(tmp)
        if eval(expr.replace(' ', '')) == 0:
            print(expr)
        return
    next_num = str(num + 1)
    # '+', '-' 삽입
    for i in range(3):
        if i == 0:
            tmp.append(' ')
        if i == 1:
            tmp.append('+')
        elif i == 2:
            tmp.append('-')
        tmp.append(next_num)
        dfs(num + 1)
        del tmp[-2:]


def operate():
    global sz
    for _ in range(tc):
        sz = int(input())
        dfs(1)
        print()


operate()
