"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns [false,1,1,2,1,3,"a",0,0]


"""


def move_zeros(array):
    l = []
    for i in array:                             # add to new list all elements,
        if isinstance(i, bool) or i != 0:       # that not equal zero
            l.append(i)
    array = l + [0] * (len(array) - len(l))     # add to the end list zeros
    return array


def move_zeros(array):
    array.sort(key=lambda x: (x == 0 and not isinstance(x, bool)))
    return array

