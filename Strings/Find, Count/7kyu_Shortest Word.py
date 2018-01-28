"""
x Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.


"""

# изначально подумал, что нужно вывести слово минимальной длины, затем перечитал условие и не стал уже убирать словарь
def find_short(s):
    words, d = s.split(), {}
    for i in words:
        d[i] = len(i)
    return min(d.values())



def find_short(s):
    return min(len(x) for x in s.split())


def find_short(s):
    return min(map(len, s.split()))




test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
