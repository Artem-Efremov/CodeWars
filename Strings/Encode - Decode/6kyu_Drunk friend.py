"""
You're hanging out with your friends in a bar, 
when suddenly one of them is so drunk, that he can't speak, 
and when he wants to say something, he writes it down on a paper. 
However, none of the words he writes make sense to you. 
He wants to help you, so he points at a beer and writes "yvvi". 
You start to understand what he's trying to say, 
and you write a script, that decodes his words.

Keep in mind that numbers, as well as other characters, 
can be part of the input, and you should keep them like they are. 
You should also test if the input is a string. 
If it is not, return "Input is not a string".

"""




from string import ascii_lowercase

def decode(string_):
    if isinstance(string_, str):
        letters = ascii_lowercase
        
        decode = {}
        for i in zip(ascii_lowercase, ascii_lowercase[::-1]):
            decode[i[0]] = i[1]
            decode[i[0].upper()] = i[1].upper()
        
        res = ''
        for i in string_:
            if i in decode:
                res += decode[i]
            else:
                res += i
        return res
    
    return "Input is not a string"





from string import ascii_lowercase as a_low
from string import ascii_uppercase as a_up

def decode(string_):
    decode_table = str.maketrans(a_low + a_up, a_low[::-1] + a_up[::-1])
    if isinstance(string_, str):
        return string_.translate(decode_table)
    return "Input is not a string"










Test.describe("Basic tests")
Test.assert_equals(decode("yvvi"), "beer")
Test.assert_equals(decode("Blf zoivzwb szw 10 yvvih"), "You already had 10 beers")
Test.assert_equals(decode("Ovg'h hdrn rm gsv ulfmgzrm!"), "Let's swim in the fountain!")
Test.assert_equals(decode({"brand": "Starobrno" }), "Input is not a string")
Test.assert_equals(decode("Tl slnv, blf'iv wifmp"), "Go home, you're drunk") 
Test.assert_equals(decode("Hfiv r xzm wzmxv lm xlk'h xzi, slow nb yvvi"), "Sure i can dance on cop's car, hold my beer")
Test.assert_equals(decode(True), "Input is not a string")
Test.assert_equals(decode("Hvv? R'n mlg gszg wifmp, r xzm hgroo gzpv nb xolgsvh luu"), "See? I'm not that drunk, i can still take my clothes off")
Test.assert_equals(decode(123), "Input is not a string")
Test.assert_equals(decode(["Beer"]), "Input is not a string")

Test.describe("Random tests")
from random import randint
base="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 .,:;?!"
sol=lambda s: "".join(["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"["zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA".index(char)] if char.isalpha() else char for char in s])

for _ in range(40):
    s="".join([base[randint(0,len(base)-1)] for x in xrange(randint(1,50))])
    Test.it("Testing for "+s)
    Test.assert_equals(decode(s),sol(s),"It should work for random inputs too")








