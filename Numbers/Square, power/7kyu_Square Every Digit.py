"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer

"""


def square_digits(num):
    squares = []
    for i in str(num):
        squares.append(int(i) ** 2)
    res = ''.join(map(str, squares))
    return int(res)




 def square_digits(num):
    res = ""
    for i in str(num):
        res += str(int(i) ** 2)
    return int(res)


 