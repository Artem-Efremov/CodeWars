"""
https://www.codewars.com/kata/plenty-of-fish-in-the-pond/python


Introduction
    Fish are an integral part of any ecosystem. Unfortunately, fish are often seen as high maintenance. Contrary to popular belief, fish actually reduce pond maintenance as they graze on string algae and bottom feed from the pond floor. They also make very enjoyable pets, providing hours of natural entertainment.
 
Driving
Task
    In this Kata you are fish in a pond that needs to survive by eating other fish. You can only eat fish that are the same size or smaller than yourself. You must create a function called fish that takes a shoal of fish as an input string. From this you must work out how many fish you can eat and ultimately the size you will grow to.
Rules
    1.  Your size starts at 1
2.  The shoal string will contain fish integers between 0-9
3.  0 = algae and wont help you feed.
4.  The fish integer represents the size of the fish (1-9).
5.  You can only eat fish the same size or less than yourself.
6.  You can eat the fish in any order you choose to maximize your size.
7.  The bigger fish you eat, the faster you grow. A size 2 fish equals two size 1 fish, size 3 fish equals three size 1 fish, and so on.
8.  Your size increments by one each time you reach the amounts below.
Increase your size
Your size will increase depending how many fish you eat and on the size of the fish. This chart shows the amount of size 1 fish you have to eat in order to increase your size.

Current size                            1   2   3   4   5   6
Amount extra needed for next size       4   8   12  16  20  24
Total size 1 fish                       4   12  24  40  60  84  
Increase to size                        2   3   4   5   6   7
 
etc...

Returns
    Return an integer of the maximum size you could be.


Example 1
shoal = "11112222"

=> 4 fish of size 1
=> 4 fish of size 2
You eat the 4 fish of size 1 (4 * 1 = 4) which increases your size to 2
Now that you are size 2 you can eat the fish that are sized 1 or 2.
You then eat the 4 fish of size 2 (4 * 2 = 8) which increases your size to 3
fish("11112222") => 3


Example 2
shoal = "111111111111"

=> 12 fish of size 1
You eat the 4 fish of size 1 (4 * 1 = 4) which increases your size to 2
You then eat the remainding 8 fish of size 1 (8 * 1 = 8) which increases your size to 3
fish("111111111111") => 3
Good luck and enjoy!


"""
















def fish(shoal):
    size = 1
    need_to_upgrade = 4  
    total_eat = 0
    for i in sorted(shoal):
        food = int(i)
        if food <= size:
            total_eat += food
            if total_eat >= need_to_upgrade:
                size += 1
                need_to_upgrade += size * 4
        else:
            break
    return size











print("Extra Tests")
test.assert_equals(fish(""), 1, "Should return '1'")
test.assert_equals(fish("0"), 1, "Should return '1'")
test.assert_equals(fish("6"), 1, "Should return '1'")
test.assert_equals(fish("1111"), 2, "Should return '2'")
test.assert_equals(fish("11112222"), 3, "Should return '3'")
test.assert_equals(fish("111122223333"), 4, "Should return '4'")
test.assert_equals(fish("111111111111"), 3, "Should return '3'")
test.assert_equals(fish("111111111111111111112222222222"), 5, "Should return '5'")
test.assert_equals(fish("151128241212192113722321331"), 5, "Should return '5'")
print("Random Tests")

def fish2(shoal):
    level = 1
    total = 0
    fishes = sorted(list(shoal))
    for fish in fishes:
        if int(fish) <= level:
            total += (1*int(fish))
            if total >= (level*4):
                total -= (level*4)
                level += 1
    return level

import random
for cwtests in range(0,91):
    fs1 = ""
    for f1 in range(0,random.randint(0,500)):
        fs1 += str(random.randint(0,9))
    print("Testing for '" + fs1 + "'")
    result = fish2(fs1)
    test.assert_equals(fish(fs1), result, "Should return '"+ str(result) + "'")