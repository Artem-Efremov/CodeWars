"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes:

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.


"""



def high_and_low(numbers):
    num = [int(i) for i in numbers.split(' ')]
    return "{} {}".format(max(num), min(num))












Test.describe("Example tests")
Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
Test.assert_equals(high_and_low("1 -1"), "1 -1");
Test.assert_equals(high_and_low("1 1"), "1 1");
Test.assert_equals(high_and_low("-1 -1"), "-1 -1");
Test.assert_equals(high_and_low("1 -1 0"), "1 -1");
Test.assert_equals(high_and_low("1 1 0"), "1 0");
Test.assert_equals(high_and_low("-1 -1 0"), "0 -1");
Test.assert_equals(high_and_low("42"), "42 42");


Test.describe("Random tests")
from random import randint as rnd
from random import shuffle

def rndtst():
    for t in range(10):
        lo = rnd(-500,500)
        hi = lo + 3000 + rnd(1,100)
        arg = [hi,lo]+[str(lo+rnd(1,2999)) for i in range(20)]
        shuffle(arg)
        arg = " ".join(str(a) for a in arg)
        exp = "%i %i"%(hi,lo)
        print(arg)
        Test.assert_equals(high_and_low(arg),exp,arg)

rndtst()
