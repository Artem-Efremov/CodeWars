"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"


"""



def likes(names):
    q_ppl = len(names)
    if q_ppl > 3:
        return "{0}, {1} and {2} others like this".format(names[0], names[1], q_ppl - 2)
    elif q_ppl == 3:
        return "{0}, {1} and {2} like this".format(names[0], names[1], names[2])
    elif q_ppl == 2:
        return "{0} and {0} like this".format(names[0], names[1])
    elif q_ppl == 1:
        return "{} likes this".format(names[0])
    else:
        return "no one likes this"
    
    
    


def likes(names):
    formats = {
                0: "no one likes this",
                1: "{} likes this",
                2: "{} and {} like this",
                3: "{}, {} and {} like this",
                4: "{}, {} and {others} others like this"
              }
    n = len(names)
    return formats[min(n,4)].format(*names, others = n - 2)








Test.describe('Basic tests')
Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

Test.describe("Random tests")
from random import randint, shuffle
sol=lambda n: 'no one likes this' if len(n)==0 else n[0]+' likes this' if len(n)==1 else n[0]+' and '+n[1]+' like this' if len(n)==2 else n[0]+', '+n[1]+' and '+n[2]+' like this' if len(n)==3 else n[0]+', '+n[1]+' and '+str(len(n)-2)+' others like this'
base=["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki", "Nene Romanova", "Nigel", "Macky Stingray", "Largo", "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol", "Daley Wong", "Galatea", "Quincy Rosenkreutz"]

for _ in xrange(40):
    shuffle(base)
    names=base[:randint(0,len(base)-1)]
    Test.it("Testig for %s" %(", ".join(names) if len(names)>0 else "none"))
    Test.assert_equals(likes(names),sol(names),"It should work for random inputs too")
    
    
    
