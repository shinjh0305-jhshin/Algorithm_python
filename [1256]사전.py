from math import comb
a, z, target = map(int, input().split())
total = a + z - 1
ans = ""


def operate():
    global total, a, z, target, ans
    if target > comb(a + z, a):
        ans = -1
        return
    while a and z:
        if_a = comb(total, z)
        if target > if_a:
            ans += 'z'
            z -= 1
            target -= if_a
        else:
            ans += 'a'
            a -= 1
        total -= 1
    if a:
        ans += 'a' * a
    else:
        ans += 'z' * z


operate()
print(ans)
