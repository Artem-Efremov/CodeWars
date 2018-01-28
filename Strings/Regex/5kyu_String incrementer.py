"""

Your job is to write a function which increments a string,
to create a new string. If the string already ends with a number, 
the number should be incremented by 1. If the string does not end 
with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros 
the amount of digits should be considered.


"""
def increment_string(strng):
    num = ''
    while strng:
        if strng[-1].isdigit():
            num = strng[-1] + num
            strng = strng[:-1]
            continue
        break
    return strng + ('1' if not num else (len(num) - len(str(int(num) + 1))) * '0' + str(int(num) + 1))




def increment_string(strng): 
    word = strng.rstrip('0123456789')
    num = strng[len(word):]
    return word + ('1' if not num else str(int(num) + 1).zfill(len(num)))




Test.assert_equals(increment_string("foo"), "foo1")
Test.assert_equals(increment_string("foobar001"), "foobar002")
Test.assert_equals(increment_string("foobar1"), "foobar2")
Test.assert_equals(increment_string("foobar00"), "foobar01")
Test.assert_equals(increment_string("foobar99"), "foobar100")
Test.assert_equals(increment_string("foobar099"), "foobar100")
Test.assert_equals(increment_string(""), "1")
