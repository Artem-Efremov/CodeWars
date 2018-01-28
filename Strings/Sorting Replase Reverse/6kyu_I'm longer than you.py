"""
https://www.codewars.com/kata/5963314a51c68a26600000ae/solutions/python

Create a function longer that accepts a string and sorts the words in it based on their respective lengths in an ascending order. If there are two words of the same lengths, sort them alphabetically. Look at the examples below for more details.

longer("Another Green World") => Green World Another
longer("Darkness on the edge of Town") => of on the Town edge Darkness
longer("Have you ever Seen the Rain") => the you Have Rain Seen ever
Assume that only only Alphabets will be entered as the input. Uppercase characters have priority over lowercase characters. That is,

longer("hello Hello") => Hello hello
Don't forget to rate this kata and leave your feedback!! Thanks

"""



def longer(s):
    words = s.split(' ')
    words.sort(key=lambda x: (len(x), x))
    return ' '.join(words)








from random import randint
Test.describe("Sample Tests")
Test.assert_equals(longer("Another Green World"), "Green World Another")
Test.assert_equals(longer("Darkness on the edge of Town"), "of on the Town edge Darkness")
Test.assert_equals(longer("Have you ever Seen the Rain"), "the you Have Rain Seen ever")
Test.assert_equals(longer("Like a Rolling Stone"), "a Like Stone Rolling")
Test.assert_equals(longer("This will be our Year"), "be our This Year will")
Test.assert_equals(longer("hello Hello"), "Hello hello")

Test.describe("Random Tests")
soln=lambda s:' '.join(sorted(sorted(s.split(" ")),key=len))


for k in range(44):
    a,b="","qwertyuiopasdfghjklzxcvbnm"
    for i in range(randint(1,5)):
        c=randint(0 ,25)
        d=randint(0 ,26)
        if c>d:c,d=d,c
        a+=b[c:d]+" "
        a = a.strip(" ")
    Test.assert_equals(longer(a),soln(a))