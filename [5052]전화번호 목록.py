import sys
Input = sys.stdin.readline
tc = int(Input())


def operate():
    for _ in range(tc):
        sz = int(Input())
        k = []
        for _2 in range(sz):
            k.append(Input().rstrip())
        k.sort()
        flag = True
        for i in range(sz - 1):
            if len(k[i + 1]) > len(k[i]) and k[i] == k[i + 1][0:len(k[i])]:
                flag = False
                break
        if not flag:
            print("NO")
        else:
            print("YES")


operate()
