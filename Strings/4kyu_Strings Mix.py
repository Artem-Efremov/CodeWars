"""
Given res strings s1 and s2, we want to visualize how different the res strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
Note for Swift, R
The prefix =: is replaced by E:

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"



"""

from string import ascii_lowercase as alph
from collections import Counter

def mix(s1, s2):
    
    res = []
    str1 = Counter(filter(str.islower, s1))
    str2 = Counter(filter(str.islower, s2))
    for i in alph:
        if i in str1 and i in str2:
            if str1[i] == str2[i] and str1[i] > 1:
                res.append('=' + ':' + str1[i] * i)
            elif str1[i] > str2[i] and str1[i] > 1:
                res.append('1' + ':' + str1[i] * i)
            elif str1[i] < str2[i] and str2[i] > 1:
                res.append('2' + ':' + str2[i] * i)
        elif i in str1 and str1[i] > 1:
            res.append('1' + ':' + str1[i] * i)
        elif i in str2 and str2[i] > 1:
            res.append('2' + ':' + str2[i] * i)
    return '/'.join(sorted(res, key=lambda x: (-len(x), x)))






# from collections import Counter

# def mix(s1, s2):
#     c1 = Counter(filter(str.islower, s1))
#     c2 = Counter(filter(str.islower, s2))
#     res = []
#     for c in set(c1.keys() + c2.keys()):
#         n1, n2 = c1.get(c, 0), c2.get(c, 0)
#         if n1 > 1 or n2 > 1:
#             res.append(('1', c, n1) if n1 > n2 else
#                 ('2', c, n2) if n2 > n1 else ('=', c, n1))
#     res = ['{}:{}'.format(i, c * n) for i, c, n in res]
#     return '/'.join(sorted(res, key=lambda s: (-len(s), s)))



# def mix(s1, s2):
#     hist = {}
#     for ch in "abcdefghijklmnopqrstuvwxyz":
#         val1, val2 = s1.count(ch), s2.count(ch)
#         if max(val1, val2) > 1:
#             which = "1" if val1 > val2 else "2" if val2 > val1 else "="
#             hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
#     return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))






# def mix(s1, s2):
#     c1 = {l: s1.count(l) for l in s1 if l.islower() and s1.count(l) > 1}
#     c2 = {l: s2.count(l) for l in s2 if l.islower() and s2.count(l) > 1}
#     r = []
#     for c in set(c1.keys() + c2.keys()):
#         n1, n2 = c1.get(c, 0), c2.get(c, 0)
#         r.append(('1', c, n1) if n1 > n2 else
#                  ('2', c, n2) if n2 > n1 else
#                  ('=', c, n1))

#     rs = ['{}:{}'.format(i, c * n) for i, c, n in r]
#     return '/'.join(sorted(rs, key=lambda s: (-len(s), s)))














# import string
# from collections import Counter


# def mix(s1, s2):
#     store = []
#     result = []

#     for i in (s1, s2):
#         store.append(Counter([x for x in i if x.islower()]))
#     for count in range(2):
#         result.append([k * v for k, v in store[count].items() if v > 1 and v >= store[(count + 1) % 2].get(k, 0)])
#         result[-1].sort()
#     return "/".join(
#         sorted(
#             ["1:{}".format(x) for x in result[0] if x not in result[1]] + ["2:{}".format(x) for x in result[1] if x not in result[0]] + ["=:{}".format(x) for x in result[0] if x in result[1]],
#             key=len,
#             reverse=True))










# {'r': 2, 'e': 4, 't': 1, 'h': 2, 'y': 1}, 
# {'y': 2, 'e': 5, 's': 1, 't': 1, 'h': 2, 'a': 1, 'r': 2}
# {'e': ['2', 5], 'h': ['=', 2], 'r': ['=', 2], 'y': ['2', 2]}

print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr", sep='\n')
print(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg", sep='\n')
print(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt", sep='\n')
print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo", sep='\n')
print(mix("codewars", "codewars"), "", sep='\n')
print(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr", sep='\n')
