k = list(input().rstrip())
qu = []


def operate():
    is_a = False
    for x in k:
        qu.append(x)
        if x == 'A':
            is_a = True
        else:
            if is_a:
                if len(qu) >= 4 and ''.join(qu[-4:]) == 'PPAP':
                    del qu[-3:]  # P를 다시 넣어야 하기에 맨 처음 P는 남겨둔다
                    is_a = False
                else:
                    break
    if not qu or ''.join(qu) == 'P':
        print('PPAP')
    else:
        print('NP')


operate()
