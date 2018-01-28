"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


"""





def valid_parentheses(string):
    d = {'(': 1, ')': -1}
    res = 0
    for i in string:
        if i in d:
            res += d[i]
            if res < 0:
                return False
    return not res




import re

_regex = "[^\(|\)]"

def valid_parentheses(string):
    string = re.sub(_regex, '', string)
    while len(string.split('()')) > 1:
        string = ''.join(string.split('()'))
    return string == ''




Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)
