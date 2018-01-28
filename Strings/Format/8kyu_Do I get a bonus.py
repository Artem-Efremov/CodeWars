"""
It's bonus time in the big city! 
The fatcats are rubbing their paws in anticipation... 
but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). 
Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. 
If bonus is false, the fatcat did not make enough money 
and must receive only his stated salary.

Return the total figure the individual will receive as a string 
prefixed with '£' (JS and Java) or '$' (C#, C++, Ruby, Clojure, 
Elixir, PHP and Python).


"""







def bonus_time(salary, bonus):
    return '${}'.format(salary * [1, 10][bonus])



def bonus_time(salary, bonus):
    return ("$%d", "$%d0")[bonus] % salary



def bonus_time(salary, bonus):
    return '${}'.format(salary * 10 ** bonus)









Test.describe("Basic tests")
Test.assert_equals(bonus_time(10000, True), '$100000')
Test.assert_equals(bonus_time(25000, True), '$250000')
Test.assert_equals(bonus_time(10000, False), '$10000')
Test.assert_equals(bonus_time(60000, False), '$60000')
Test.assert_equals(bonus_time(2, True), '$20')
Test.assert_equals(bonus_time(78, False), '$78')
Test.assert_equals(bonus_time(67890, True), '$678900')

Test.describe("Random tests")
from random import randint
sol=lambda s, b: "$%s" %(s*(10 if b else 1))

for _ in xrange(40):
    s=randint(1,10**randint(2,4))*100; b=[False, True][randint(0,1)]
    Test.it("Testing for %s and %s" %(s,b))
    Test.assert_equals(bonus_time(s,b),sol(s,b),"It should work for random inputs too")
