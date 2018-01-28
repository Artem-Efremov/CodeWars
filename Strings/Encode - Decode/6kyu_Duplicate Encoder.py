 
"""
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("


Notes:

There is a flaw in the JS version, that may occur in the random tests. Do not hesitate to do several attempts before modifying your code if you fail there.

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is actually the expected result, not the input! (these languages are locked so that's not possible to correct it).


"""


def duplicate_encode(word):
    d, res = {}, ''
    word = word.lower()
    for i in word:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in word:
        if d[i] > 1:
            res += ')'
        else:
            res += '('
    return res



def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


def duplicate_encode(word):
    word = word.lower()
    return ''.join(('(' if Counter(word)[c] == 1 else ')') for c in word)




Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("CodeWarrior"),"()(((())())")
Test.assert_equals(duplicate_encode("Supralapsarian"),")()))()))))()(","should ignore case")
Test.assert_equals(duplicate_encode("iiiiii"),"))))))","duplicate-only-string")
Test.assert_equals(duplicate_encode("(( @"),"))((")
Test.assert_equals(duplicate_encode(" ( ( )"),")))))(")
