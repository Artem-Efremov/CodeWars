"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of ProjectEuler.net

"""




def solution(number):
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    
    return result







test.describe("Multiples of 3 and 5")

test.it("should handle basic cases")
test.assert_equals(solution(10), 23)
test.assert_equals(solution(20), 78)

test.it("should handle zeroes")
test.assert_equals(solution(0), 0)
test.assert_equals(solution(1), 0)

test.it("should handle large numbers")
test.assert_equals(solution(200), 9168)