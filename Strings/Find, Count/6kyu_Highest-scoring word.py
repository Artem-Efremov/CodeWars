"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.



"""




def high(x):
    a = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    d = {}
    for i in x.split():
        score = 0
        for j in i:
            score += a[j]
        d[i] = score
    b = list(d.items())
    b.sort(key=lambda x: x[1], reverse =True)
    return b[0][0]



def high(x): 
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def high(x):
    a = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    d = {}
    for i in x.split():
        score = 0
        for j in i:
            score += a[j]
        d[i] = score 
    return max(d, key=d.get)




test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
test.assert_equals(high('massage yes massage yes massage'), 'massage')
test.assert_equals(high('take two bintang and a dance please'), 'bintang')
