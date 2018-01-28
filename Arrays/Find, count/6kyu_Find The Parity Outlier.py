"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)

"""


def find_outlier(array):
    tag = ['odd' if i % 2 else 'even' for i in array]
    ind = tag.index('odd') if tag.count('odd') == 1 else tag.index('even')
    return array[ind]



def find_outlier(array):
    tag = [i % 2 for i in array]
    ind = tag.index(0) if tag.count(0) == 1 else tag.index(1)
    return array[ind]



def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]



