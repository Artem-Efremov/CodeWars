"""
##Do you know how to write a recursive function? Let's test it!
Definition: Recursive function is a function that calls itself during its execution

Classic factorial counting on Javascript
function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n-1) 
}
Your objective is to complete a recursive function reverse() that receives str as String and returns the same string in reverse order

Rules:

reverse function should be executed only N times. N = length of the input string
helper functions are not allowed
changing the signature of the function is not allowed
Examples:

reverse("hello world") = "dlrow olleh" (N = 11)
reverse("abcd") = "dcba" (N = 4)
reverse("12345") = "54321" (N = 5)
All tests for this Kata are randomly generated, besides checking the reverse logic they will count how many times the reverse() function has been executed.

Please note that tests for
js
and
coffeescript
and
Java "Hello world"
show wrong messages. 
Expected and Actual values should be swapped. 
Unfortunately Test Cases section is blocked for editing and can be changed only by moderator.

"""


def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]









import unittest
import random

def test_f(str):
	return str if len(str) == 1 else test_f(str[1:]) + str[:1];

class Counter(object) :
    def __init__(self, fun) :
        self._fun = fun
        self.counter=0
    def __call__(self,*args, **kwargs) :
        self.counter += 1
        return self._fun(*args, **kwargs)

reverse = Counter(reverse)

def generator(n):
	symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

	word = "";
	for i in range(0, n):
		word += symbols[random.randint(0, len(symbols) -1)]

	return word;


def test_random():
	test.it("Randomly generated tests")
	for i in range(1, 31): 
		word = generator(i);
		reverse.counter = 0
		test.assert_equals(test_f(word), reverse(word))
		test.assert_equals(len(word), reverse.counter)

test_random()
