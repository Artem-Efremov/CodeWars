"""
Description:
DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining lowercase, same like you see in the newspaper.

But for a change lets do that for each and every word of the given String. Your task is to capitalize very word that has length greater than 2, leaving smaller words as they are.

*should work also on Leading and Trailing Spaces and caps.

drop_cap('apple') => "Apple"
drop_cap('apple of banana'); => "Apple of Banana"
drop_cap('one   space'); => "One   Space" 
drop_cap('   space WALK   '); => "   Space Walk   "
Note: you will be provided atleast one word and should take string as input and return string as output.

"""


import re
def drop_cap(text):
    words = text.split()
    words = filter(lambda x: len(x) > 2, words)
    drop_caps = [i.capitalize() for i in words]
    for a, b in zip(words, drop_caps):
        text = re.sub(a, b, text)
    return text



import re
def drop_cap(text):
    words = re.findall(r'\s?(\w+)\s?', text)
    words = filter(lambda x: len(x) > 2, words)
    drop_caps = [i.capitalize() for i in words]
    for a, b in zip(words, drop_caps):
        text = re.sub(a, b, text)
    return text





   Test.describe("Basic tests")
Test.assert_equals(drop_cap('Apple Banana'),"Apple Banana")
Test.assert_equals(drop_cap('Apple'),"Apple")
Test.assert_equals(drop_cap(''),"")
Test.assert_equals(drop_cap('of'),"of")
Test.assert_equals(drop_cap('Revelation of the contents outraged American public opinion, and helped generate'),"Revelation of The Contents Outraged American Public Opinion, And Helped Generate")
Test.assert_equals(drop_cap('more  than    one space between words'),"More  Than    One Space Between Words")
Test.assert_equals(drop_cap('  leading spaces'),"  Leading Spaces")
Test.assert_equals(drop_cap('trailing spaces   '),"Trailing Spaces   ")
Test.assert_equals(drop_cap('ALL CAPS CRAZINESS'),"All Caps Craziness")
Test.assert_equals(drop_cap('rAnDoM CaPs CrAzInEsS'),"Random Caps Craziness")

Test.describe("Random tests")
from random import randint
import re
base="abcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZ   "
drop_sol=lambda s: re.sub("\S+",lambda x: x.group(0).capitalize() if len(x.group(0))>2 else x.group(0) ,s)

for _ in xrange(40):
    s="".join([base[randint(0,len(base)-1)] for i in xrange(randint(1,40))])
    s=re.sub("\s{2,100}"," ",s).strip()
    if s=="": s="CodeWars"
    Test.it("Testing for "+repr(s))
    Test.assert_equals(drop_cap(s),drop_sol(s),"It should work for random inputs too")