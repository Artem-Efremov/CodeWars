"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.


"""


def find_it(seq):
    d = {}
    for i in seq:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i,j in d.items():
        if j % 2 != 0:
            return i
        


def find_it(seq):
    d = {}
    for i in set(seq):
        d[i] = seq.count(i)
    for i,j in d.items():
        if j % 2 != 0:
            return i
        
        
        
def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2 != 0:
            return i
        


def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i








test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
