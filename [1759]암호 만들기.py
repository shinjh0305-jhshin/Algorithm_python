from itertools import combinations
words, sz = map(int, input().split())
k = list(input().split())


def operate():
    k.sort()
    for tmp in combinations(k, words):
        vowels = 0
        consonants = 0
        for x in tmp:
            if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                vowels += 1
            else:
                consonants += 1
        if vowels >= 1 and consonants >= 2:
            print(*tmp, sep='')


operate()