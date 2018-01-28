"""
You are given a string of n lines, each substring being n characters long. For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study the "horizontal" and the "vertical" scaling of this square of strings.

A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
A v-vertical scaling of a string consists of replicating v times each part of the squared string.

Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

Example: a = "abcd\nefgh\nijkl\nmnop"
scale(a, 2, 3) --> "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
Printed:

abcd   ----->   aabbccdd
efgh            aabbccdd
ijkl            aabbccdd
mnop            eeffgghh
                eeffgghh
                eeffgghh
                iijjkkll
                iijjkkll
                iijjkkll
                mmnnoopp
                mmnnoopp
                mmnnoopp
#Task:

Write function scale(strng, k, v) k and v will be positive integers. If strng == "" return "".

"""







def scale(strng, k, n):
    if strng:
        parts = []
        for i in strng.split('\n'):
            item = ''
            for j in i:
                item += j * k
            for m in range(n):
                parts.append(item)
        strng = '\n'.join(parts)
    return strng



















def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("scale")
Test.it("Basic tests")
a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
testing(scale(a, 2, 3), r)

testing(scale("", 5, 5), "")

testing(scale("Kj\nSH", 1, 2),"Kj\nKj\nSH\nSH")

testing(scale("lxnT\nqiut\nZZll\nFElq", 1, 2), "lxnT\nlxnT\nqiut\nqiut\nZZll\nZZll\nFElq\nFElq")

r = ("YYVVjjoossWW\nYYVVjjoossWW\nHHGGhhKKGGZZ\nHHGGhhKKGGZZ\nLLHHNNMMLLmm\nLLHHNNMMLLmm\nJJttccWWCCjj\n"
        "JJttccWWCCjj\nggVVttjjyykk\nggVVttjjyykk\nOOJJBBkkOOKK\nOOJJBBkkOOKK")
testing(scale("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 2, 2), r)

r = "YVjosW\nYVjosW\nHGhKGZ\nHGhKGZ\nLHNMLm\nLHNMLm\nJtcWCj\nJtcWCj\ngVtjyk\ngVtjyk\nOJBkOK\nOJBkOK"
testing(scale("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 1, 2), r)

testing(scale("WgaB\nMmIn\nqJwv\nAhho", 2, 1), "WWggaaBB\nMMmmIInn\nqqJJwwvv\nAAhhhhoo")

testing(scale("CG\nla", 2, 3), "CCGG\nCCGG\nCCGG\nllaa\nllaa\nllaa")    

from random import randint

def one213(s, k):
    return "".join(map (lambda z : z * k, list(s)))
def scale_sol213(strng, k, n):
    if (len(strng) == 0): return ""
    newstr0 = map (lambda x : one213(x, k), strng.split("\n"))
    newstr1 = map (lambda y: (y + "\n") * n, newstr0)
    return "".join(newstr1)[0:-1]

def do_ex(k):
    if (k % 2 == 1): k += 1
    j , res = 0, []
    while (j < k):
        s, i = "", 0
        while (i < k):
            if (randint(0, 100) % 2 == 0): s += chr(randint(97, 122))
            else: s += chr(randint(65, 90))
            i += 1
        res.append(s)
        j += 1
    return "\n".join(res)

def tests_code():
    print("Random tests scale")
    i = 0
    while (i < 200):
        s = do_ex(randint(3, 6))
        k = randint(2, 3)
        n = k + 1
        testing(scale(s, k, n), scale_sol213(s, k, n))
        i += 1
tests_code()




