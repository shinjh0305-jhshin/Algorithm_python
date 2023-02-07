sz = int(input())
k = list(map(int, input().split()))


def operate():
    k.sort()
    cur_max = 0
    for x in k:
        if cur_max >= x - 1:
            cur_max = cur_max + x
        else:
            break
    print(cur_max + 1)


operate()