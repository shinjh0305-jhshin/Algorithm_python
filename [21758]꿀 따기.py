sz = int(input())
k = list(map(int, input().split()))
acc_sum = [0] * sz
ans = -1


def type1():
    global ans
    all_sum = sum(k)
    acc_sum[0] = k[0]
    for i in range(1, sz):
        acc_sum[i] = acc_sum[i - 1] + k[i]

    for i in range(1, sz):
        tmp = all_sum * 2 - (k[0] + k[i] + acc_sum[i])
        ans = max(ans, tmp)


def type2():
    global ans
    new_arr = k[1:-1]
    ans = max(ans, sum(new_arr) + max(new_arr))


def operate():
    # 벌 벌 벌통
    type1()
    # 벌통 벌 벌
    k.reverse()
    type1()
    # 벌 벌통 벌
    type2()
    print(ans)


operate()