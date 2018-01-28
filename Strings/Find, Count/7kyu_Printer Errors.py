"""
In a factory a printer prints labels for boxes. 
For one kind of boxes the printer has to use colors which, 
for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. 
For example a "good" control string would be aaabbbbhaijjjm meaning 
that the printer used three times color a, four times color b, 
one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction 
and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

You have to write a function printer_error which given a string 
will output the error rate of the printer as a string representing 
a rational whose numerator is the number of errors and the denominator 
the length of the control string. Don't reduce this fraction 
to a simpler expression.

The string has a length greater or equal to one and contains 
only letters from ato z.

#Examples:

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"


"""

def printer_error(s):
    errors = 0 
    for i in s:
        if ord(i) not in range(ord('a'), ord('m') + 1):     # if i > "m":
            errors += 1
    return '{0}/{1}'.format(errors, len(s))




import re
def printer_error(s):
    errors = re.sub("[a-m]",'',s)
    return "{}/{}".format(len(errors),len(s))










Test.describe("printer_error")
Test.it("Basic tests")
s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
Test.assert_equals(printer_error(s), "3/56")
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
Test.assert_equals(printer_error(s), "6/60")
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
Test.assert_equals(printer_error(s) , "11/65")

from random import randint

def do_ex():
    i = 0
    res = ""
    k = randint(10, 500)
    while (i < k):
        n = randint(97, 109)
        res += chr(n)
        i += 1
    while (i < 2 * k):
        if (i % 17 == 0):
            n = randint(110, 122) 
        else:
            n = randint(97, 109)
        res += chr(n)
        i += 1
    return res
def printer_error_sol(s):
    cnt, l = 0, 0
    for c in s:
        l += 1
        if 109 < ord(c) <= 122:
            cnt += 1
    return str(cnt) + "/" + str(l)
def tests():
    print("Random tests ****************** ")
    i = 0
    while (i < 200):
        s = do_ex()
        Test.assert_equals(printer_error(s), printer_error_sol(s))
        i += 1
tests()
