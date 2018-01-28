"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false


"""



def xo(s):
    d, s = {'x': 0, 'o': 0}, s.lower()
    for i in s:
        if i not in d:
            continue
        else:
            d[i] += 1
    return d['x'] == d['o']






def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')





from collections import Counter

def xo(s):
    d = Counter(s.lower())
    return d.get('x', 0) == d.get('o', 0)





Test.expect(xo('xo'))
Test.expect(xo('XO'))
Test.expect(xo('xo0'))
Test.expect(not xo('xxxoo'))
Test.expect(xo(''),'Empty string contains equal amount of x and o');
Test.expect(xo('xxxxxoooxooo'));
Test.expect(xo('xxxxxoooXooo'),'Comparison is case-insensitive');
Test.expect(xo('abcdefghijklmnopqrstuvwxyz'),'Alphabet contains equal amount of x and o')
