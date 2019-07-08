

def anagram2(s1, s2):
    word1 = sorted(s1.replace(" ", ""))
    word2 = sorted(s2.replace(" ", ""))
    if word1 == word2:
        print("True")
    else:
        print("False")


def anagram1(s1, s2):
    word1 = s1.replace(" ", "")
    word2 = s2.replace(" ", "")
    letter_count = dict()

    for char in word1:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1

    for char in word2:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] -= 1

    print(all(value == 0 for value in letter_count.values()))





anagram1('go go go' ,'gggooo')
anagram1('abc','cba')
anagram1('hi man' ,'hi     man')
anagram1('aabbcc' ,'aabbc')
anagram1('123' ,'1 2')
anagram1('dog','go2d')
anagram1('clint eastwood','old west action')
