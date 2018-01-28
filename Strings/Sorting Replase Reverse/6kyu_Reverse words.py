 
"""
Write a reverseWords function that accepts a string a parameter, 
and reverses each word in the string. 
Any spaces in the string should be retained.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
reverse_words("double  spaces") # returns  "elbuod  secaps"


"""

Если не указать явно в split() пробел (' '), то придется мучиться долго:

def reverse_words(s):
    words = list(''.join([i[::-1] for i in s.split()]))
    [words.insert(i, ' ') for i in [i for i in range(len(s)) if s[i] == ' ']]
    return ''.join(words)



def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))




import re
def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)


def reverse_words(str):
    for word in str.split():
        str = str.replace(word, word[::-1])
    return str




test.assert_equals(reverse_words('This  is an  example!'),'sihT  si na  !elpmaxe');
