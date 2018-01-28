"""
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

"""



def find_missing_letter(chars):
    nums = list(map(ord, chars))
    for i in range(nums[0], nums[-1] + 1):
        if i not in nums:
            return chr(i)









test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
test.assert_equals(find_missing_letter(['b','d']), 'c')

import random
import string

test_alphas = [string.ascii_uppercase, string.ascii_lowercase]
test.it("random tests")
for i in range(30):
    alpha = random.choice(test_alphas)
    start = random.randint(0, 22)
    end = random.randint(start + 3, 25)
    miss = random.randint(start +1, end -1)
    tvals = [alpha[j] for j in range(start, end +1) if j != miss]
    test.assert_equals(find_missing_letter(tvals), alpha[miss])