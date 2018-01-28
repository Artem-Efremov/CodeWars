"""
Description:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

"""




def unique_in_order(seq):
    ind = 0
    res = []
    if seq:
        res.append(seq[0])
        if len(seq) > 1:
            for i in seq[1:]:
                if i != res[ind]:
                    res.append(i)
                    ind += 1
    return res





def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result






from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]





def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res












test.it("should work with empty array")
test.assert_equals(unique_in_order(''),[])
test.it("should work with one element")
test.assert_equals(unique_in_order('A'),['A'])
test.it("should reduce duplicates")
test.assert_equals(unique_in_order('AA'),['A'])        
test.assert_equals(unique_in_order('AAAABBBCCDAABBB'),['A', 'B', 'C', 'D', 'A', 'B'])
test.assert_equals(unique_in_order('AADD'),['A','D'])
test.assert_equals(unique_in_order('AAD'),['A','D'])
test.assert_equals(unique_in_order('ADD'),['A','D'])
test.it("and treat lowercase as different from uppercase")
test.assert_equals(unique_in_order('ABBCcAD'),['A', 'B', 'C', 'c', 'A', 'D'])
test.it("and work with int arrays")
test.assert_equals(unique_in_order([1,2,3,3]),[1,2,3])
test.it("and work with char arrays")
test.assert_equals(unique_in_order(['a','b','b']),['a','b'])