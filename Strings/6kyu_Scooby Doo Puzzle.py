"""
Introduction
 	Good one Shaggy! We all love to watch Scooby Doo, Shaggy Rogers, Fred Jones, Daphne Blake and Velma Dinkley solve the clues and figure out who was the villain. The story plot rarely differed from one episode to the next. Scooby and his team followed the clue then unmasked the villain at the end.
 
Scooby Doo
Task
 	Your task is to initially solve the clues and then use those clues to unmask the villain. You will be given a string of letters that you must manipulate in a way that the clues guide you. You must then output the villain.
 
You will be given an Array of potential villains and you must only return the correct masked villain.

 	Potential Villains for the example test cases
Black Knights, Puppet Master, Ghost Clowner, Witch Doctors, Waxed Phantom, Manor Phantom, Ghost Bigfoot, Haunted Horse, Davy Crockett, Captain Injun, Greens Gloobs, Ghostly Manor, Netty Crabbes, King Katazuma, Gators Ghouls, Headless Jack, Mambas Wambas, Medicines Man, Demon Sharker, Kelpy Monster, Gramps Vamper, Phantom Racer, Skeletons Men, Moon Monsters
 
There will be different villains for the main test cases!

 	Clue 1: The first clue is in a 'house' on 'String Class' Avenue.
 
Good luck!

"""


# Clue 1: The first clue is in a 'house' on 'String Class' Avenue.

# def scoobydoo(villian, villians):
#     x = String()
#     x.house()

# """
# Step 1: Rotate all letters to the right by 5
# Clue: You are close to the monster so you may need to create a 'Disguise'
# """

# # Step 2:
# def scoobydoo(villian, villians):
#     x = Disguise()

# """
# Step 2: Reverse the whole string
# Clue: What is the length of Scooby Doo's favourite snack?
# Try using the answer in the Integer Class
# """

# # Step 3:
# def scoobydoo(villian, villians):
#     x = Integer()
#     """dog biscuit"""
#     x.eleven()

"""
Step 3: Add 5 letters onto every even letter in the Villans Name ie a=>f
Make sure after the letter z it goes round to a
"""


def char_shift_a_z(char, shift=5):
    return chr((ord(char) - 96 + shift) % 26 + 96)




def scoobydoo(villian, villians):
    
    merged_vil = [i.replace(' ', '').lower() for i in villians]
    conv_table = dict(zip(merged_vil, villians))
    
    step_1 = villian[-5:] + villian[:-5]            # 1. Rotate all letters to the right by 5
    
    step_2 = step_1[::-1]                           # 2. Reverse the whole string

    step_3 = ''                                     # 3. Add 5 letters onto every even letter in the Villans Name ie a=>f
    pos = 1                                         #    Make sure after the letter z it goes round to a
    for i in step_2:
        if pos % 2 == 0 and i.isalpha():
            step_3 += chr((ord(i) - 97 + 5) % 26 + 97)
        else:
            step_3 += i
        pos += 1
        
    return conv_table[step_3]





def scoobydoo(villian, villians):
    return [v for v in villians if villian[-6:0:-2] in v[::2]][0]














import random

def scoobydooreverse(villian):
    villian = ''.join(villian.split(' ')).lower()
    badguy = ""
    num = 0
    for le in villian:
        num += 1
        if num % 2 == 0:
            le = le.translate(str.maketrans('fghijklmnopqrstuvwxyzabcde','abcdefghijklmnopqrstuvwxyz'))
        badguy += le
    villian = badguy
    villian = villian[::-1]
    villian = ''.join(shift(villian, -5))
    return villian

def scoobydoo2(villian, villians):
    villian = villian.lower()
    villian = ''.join(shift(villian, 5))
    villian = villian[::-1]
    badguy = ""
    num = 0
    for le in villian:
        num += 1
        if num % 2 == 0:
            le = le.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz','fghijklmnopqrstuvwxyzabcde'))
        badguy += le

    for bg in villians:
        if ''.join(bg.lower().split(' ')) == badguy: return bg

letters = "abcdefghijklmnopqrstuvwxwz"
for rtest in range(100):
    villians = []
    for le in range(20):
        vil = ""
        for le in range(20):
            vil += letters[random.randint(0,len(letters)-1)]
        villians.append(vil)
    n = random.randint(0,len(villians)-1)
    bb = scoobydooreverse(villians[n])
    solution = scoobydoo2(bb,villians)
    result = scoobydoo(bb,villians)
    test.it("Should return: "+solution)
    test.assert_equals(result, solution)
