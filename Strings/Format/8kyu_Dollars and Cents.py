"""
The company you work for has just been awarded a contract to build a payment gateway. In order to help move things along, you have volunteered to create a function that will take a float and return the amount formatting in dollars and cents.

39.99 becomes $39.99

The rest of your team will make sure that the argument is sanitized before being passed to your function although you will need to account for adding trailing zeros if they are missing (though you won't have to worry about a dangling period).

Examples:

3 needs to become $3.00

3.1 needs to become $3.10

Good luck! Your team knows they can count on you!


"""




def format_money(amount):
    return '${:.2f}'.format(amount)








def tester328174(sample):
  Test.it('Testing %s' % sample)
  Test.assert_equals(format_money(sample), '$%0.2f' % sample, "That's not formatted the way we expected")
  
Test.describe('Fixed tests')
for sample in (39.99, 3, 3.10, 314.16):
    tester328174(sample)

Test.describe('Random tests')
from random import random
for eiuqoiuwr838 in range(1, 10):
  tester328174(int(random() * eiuqoiuwr838 * 100))
for eiuqoiuwr838 in range(1, 19):
  tester328174(int(random() * eiuqoiuwr838 * 1000)/10.0)
for eiuqoiuwr838 in range(1, 12):
  tester328174(int(random() * eiuqoiuwr838 * 10000)/100.0)
