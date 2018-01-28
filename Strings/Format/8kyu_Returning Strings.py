"""
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]

"""



def greet(name):
    text = "Hello, {} how are you doing today?"
    return greet.format(text)






import random

Test.it('Basic tests')
Test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
Test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")

def randgen_sent():
    rand = random.randint(10, 50)
    base = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,'
    sent = ''.join(random.choice(base) for i in range(rand))
    print(sent)
    return sent 

actual=lambda s: "Hello, {} how are you doing today?".format(s)

Test.it('Random tests')
for i in range(100):
    string = randgen_sent()
    expected = actual(string)
    Test.assert_equals(greet(string), expected)

