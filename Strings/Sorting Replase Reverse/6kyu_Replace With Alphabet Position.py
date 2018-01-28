"""
In this kata you are required to, given a string, 
replace every letter with its position in the alphabet.

If anything in the text isn't a letter, 
ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.

"""



def alphabet_position(text):
    return ' '.join(str(ord(i.lower()) - 96) for i in text if i.isalpha())











import string
import random
def ap(text):
        text = text.lower().strip()
        return " ".join([str(ord(x) - ord("a") + 1) for x in text if x in string.ascii_letters] )

print("Tests for each letter:")
for letter in string.ascii_lowercase:
    test.assert_equals(alphabet_position(letter), ap(letter))
print("Randomly generated tests:")
for i in range(100):
    x = ""
    for j in range(6):
        x += random.choice(string.ascii_lowercase)
    print("Testing \"{0}\":".format(x))
    test.assert_equals(alphabet_position(x), ap(x))
print("Number tests:")
for i in range(15):
    n = ""
    for l in range(10):
        n += str(random.randint(1, 9))
    test.assert_equals(alphabet_position(n), ap(n))
