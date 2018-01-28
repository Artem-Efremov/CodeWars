"""
Create a function named divisors/Divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

You can assume that you will only get positive integers as inputs.


"""



def divisors(integer):
    array = []
    for i in range(2, integer):
        if integer % i == 0:
            array.append(i)
    return '{} is prime'.format(integer) if len(array) == 0 else array




test.assert_equals(divisors(15), [3,5])
test.assert_equals(divisors(253), [11,23])
test.assert_equals(divisors(24), [2,3,4,6,8,12])
test.assert_equals(divisors(13), "13 is prime")
test.assert_equals(divisors(3), "3 is prime")
test.assert_equals(divisors(29), "29 is prime")
