st = input().rstrip()
t = input().rstrip()


def strip(s=0, e=len(t) - 1, rev=False):
    if e - s + 1 == len(st):
        if (rev and ''.join(reversed(t[s:e + 1])) == st) or (not rev and t[s:e + 1] == st):
            return True
        else:
            return False
    if not rev:
        if (t[e] == 'A' and strip(s, e - 1, False)) or (t[s] == 'B' and strip(s + 1, e, True)):
            return True
    else:
        if (t[s] == 'A' and strip(s + 1, e, True)) or (t[e] == 'B' and strip(s, e - 1, False)):
            return True
    return False


print(int(strip()))
