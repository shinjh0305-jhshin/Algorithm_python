def generate(num):  # num을 생성자로 하는 숫자 구하기
    ans = num
    while num:
        ans += num % 10
        num //= 10
    return ans


def operate():
    res = [True] * 10001
    for i in range(1, 10001):
        num = generate(i)
        if num <= 10000:
            res[num] = False
    ans = list(filter(lambda x: res[x], range(1, 10001)))
    print(*ans, sep='\n')


operate()
