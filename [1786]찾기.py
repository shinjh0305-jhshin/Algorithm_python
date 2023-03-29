str = input().rstrip()
pat = input().rstrip()
failure = [0] * len(pat)
ans = []


def get_failure():
    i, j = 0, 1
    failure[0] = -1

    while j < len(pat):
        while True:
            # Match!
            if pat[i] == pat[j]:
                failure[j] = i
                i += 1
                break

            # No match!
            if i == 0:
                failure[j] = -1
                break
            else:
                i = failure[i - 1] + 1
        j += 1


def get_match():
    str_mov, pat_mov = 0, 0

    while str_mov < len(str) and pat_mov < len(pat):
        if str[str_mov] == pat[pat_mov]:
            str_mov += 1
            pat_mov += 1
        elif pat_mov == 0:
            str_mov += 1
        else:
            pat_mov = failure[pat_mov - 1] + 1

        if pat_mov == len(pat):
            ans.append(str_mov - len(pat) + 1)
            pat_mov = failure[pat_mov - 1] + 1

    print(len(ans))
    print(*ans)


get_failure()
get_match()
