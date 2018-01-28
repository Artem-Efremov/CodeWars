"""
Write a function, persistence, that takes in a positive parameter num 
and returns its multiplicative persistence, which is the number of times 
you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.

 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number


"""

def persistence(n):
    num = list(str(n))
    q = 0
    while len(num) > 1:
        m = 1
        for i in num:
            m *= int(i)
        q += 1
        num = list(str(m))
    return q



from operator import mul
def persistence(n):
    i = 0
    while n>=10:
        n = reduce(mul,[int(x) for x in str(n)], 1)
        i+=1
    return i



from operator import mul
def persistence(n):
    return 0 if n < 10 else persistence(reduce(mul, [int(i) for i in str(n)], 1)) + 1   #  [int(i) for i in str(n)]  =>  list(map(int, list(str(n))))



Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)
