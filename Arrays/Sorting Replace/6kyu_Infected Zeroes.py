"""
In this kata, the number 0 is infected. You are given a list. Every turn, any item in the list that is adjacent to a 0 becomes infected and transforms into a 0. How many turns will it take for the whole list to become infected?

[0,1,1,0] ==> [0,0,0,0] 
All infected in 1 turn.

[1,1,0,1,1] --> [1,0,0,0,1] --> [0,0,0,0,0]
All infected in 2 turns

[0,1,1,1] --> [0,0,1,1] --> [0,0,0,1] --> [0,0,0,0]
All infected in 3 turns.
All lists will contain at least one item, and at least one zero, and the only items will be 0s and 1s. Lists may be very very long, so pure brute force approach will not work.


"""




def infected_zeroes(lst):
    txt = ''.join(str(i) for i in lst)
    healthy = txt.split('0')
    a = []
    for i in healthy:
        a.append(len(i) + 1)
    start = txt.find('0') * 2
    end = txt[::-1].find('0') * 2
    b = [start, end]
    return max(a + b) // 2


print(infected_zeroes([0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]))





def infected_zeroes(lst):
    nonzero_streak = 0
    overall_longest = 0
    for i in lst:
        if i == 0:
            nonzero_streak = 0
        else:
            nonzero_streak += 1
            overall_longest = max(overall_longest, nonzero_streak)
    
    if overall_longest == 0: return 0
    center = (overall_longest+1) >> 1 
    left  = 0
    right = 0
    while lst[left] != 0: left += 1
    while lst[right-1] != 0: right -= 1
    return max(left, center, -right)







from re import sub
from math import ceil


def infected_zeroes(lst):
    # convert out list to a string for processing and split on "infected" zeroes
    chunks_of_ones = ''.join([str(l) for l in lst]).split('0')

    longest_chunk_of_ones = max([len(c) for c in chunks_of_ones])

    # if our longest run is the starting or ending chunk, num_turns is going to be the length of that chunk
    # however, all other chunks will be getting infected from both sides, so in those cases we divide by two
    num_turns = max(len(chunks_of_ones[0]), ceil(longest_chunk_of_ones / 2), len(chunks_of_ones[-1]))
    
    return num_turns