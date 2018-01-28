"""
Introduction
    Slot machine (American English), informally fruit machine (British English), puggy (Scottish English slang), the slots (Canadian and American English), poker machine (or pokies in slang) (Australian English and New Zealand English) or simply slot (American English), is a casino gambling machine with three or more reels which spin when a button is pushed. Slot machines are also known as one-armed bandits because they were originally operated by one lever on the side of the machine as distinct from a button on the front panel, and because of their ability to leave the player in debt and impoverished. Many modern machines are still equipped with a legacy lever in addition to the button. (Source Wikipedia)
 

Task
    You will be given three reels of different images and told at which index the reels stop. From this information your job is to return the score of the resulted reels.
Rules
    1. There are always exactly three reels
2. Each reel has 10 different items.
3. The three reel inputs may be different.
4. The spin array represents the index of where the reels finish.
5. The three spin inputs may be different
6. Three of the same is worth more than two of the same
7. Two of the same plus one "Wild" is double the score.
8. No matching items returns 0.
Scoring
Item
Three of the same
Two of the same
Two of the same plus one Wild
Wild
100
10
N/A
Star
90
9
18
Bell
80
8
16
Shell
70
7
14
Seven
60
6
12
Cherry
50
5
10
Bar
40
4
8
King
30
3
6
Queen
20
2
4
Jack
10
1
2
 
Returns
    Return an integer of the score.
Example
Initialise
reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel3 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [5,5,5]
result = fruit([reel1,reel2,reel3],spin)
Scoring
reel1[5] == "Cherry"
reel2[5] == "Cherry"
reel3[5] == "Cherry"

Cherry + Cherry + Cherry == 50
Return
result == 50
Good luck and enjoy!

"""





def fruit(reels, spins):
    
    # 1. Initialization
    scoring = {'Wild': 10, 'Star': 9, 'Bell': 8, 'Shell': 7, 'Seven': 6, 
               'Cherry': 5, 'Bar': 4, 'King': 3, 'Queen': 2, 'Jack': 1}

    received_items = {}
    for i in range(3):
        item = reels[i][spins[i]]
        if item not in received_items:
            received_items[item] = 1
        else:
            received_items[item] += 1
    
    dif_items = len(received_items)

    if dif_items == 3:
        score = 0
    elif dif_items == 1:
        triple = list(received_items)[0]
        score = scoring[triple] * 10
    else:
        for i in received_items:
            if received_items[i] == 2:
                double = i
        if 'Wild' in received_items and double != 'Wild':
            score = scoring[double] * 2
        else:
            score = scoring[double]


    return score






from collections import Counter

ORDER = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
VALUES = {name: i+1 for i,name in enumerate(ORDER[::-1])}

def fruit(reels, spins):
    counts = { c:v for v,c in Counter([ VALUES[r[i]] for r,i in zip(reels, spins) ]).items() }
    return counts.get(3,0)*10 + counts.get(2,0) * 2**(counts.get(1,0)==10)










def fruit(reels, spins):
    result = sorted( reels[i][spins[i]] for i in range(3) )
    SCORES = {'Wild': 10, 'Star': 9, 'Bell': 8, 'Shell': 7, 'Seven': 6,
          'Cherry': 5, 'Bar': 4, 'King': 3, 'Queen': 2, 'Jack': 1 }
    
    if len(set(result)) == 1:
        return SCORES[result[0]] * 10
    
    elif len(set(result)) == 2:
        return SCORES[result[1]] * ((result[1] != result[2] == 'Wild') + 1)
    
    else:
        return 0












reelz = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spinz = [5,5,5]
test.it("Should return: '50'")
test.assert_equals(fruit([reelz,reelz,reelz],spinz), 50, "Should return: '50'")
reel1z = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2z = ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"]
reel3z = ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"]
spinz = [0,1,2]
test.it("Should return: '100'")
test.assert_equals(fruit([reel1z,reel2z,reel3z],spinz), 100, "Should return: '100'")
reel1z = ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"]
reel2z = ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"]
reel3z = ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"]
spinz = [9,8,7]
test.it("Should return: '10'")
test.assert_equals(fruit([reel1z,reel2z,reel3z],spinz), 10, "Should return: '10'")
reel1z = ["King", "Jack", "Wild", "Bell", "Star", "Seven", "Queen", "Cherry", "Shell", "Bar"]
reel2z = ["Star", "Bar", "Jack", "Seven", "Queen", "Wild", "King", "Bell", "Cherry", "Shell"]
reel3z = ["King", "Bell", "Jack", "Shell", "Star", "Cherry", "Queen", "Bar", "Wild", "Seven"]
spinz = [0,5,0]
test.it("Should return: '6'")
Test.assert_equals(fruit([reel1z,reel2z,reel3z],spinz), 6, "Should return: '6'")

def fruitSolveIt(reels, spins):
    reel = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
    items = [reels[0][spins[0]]][0], [reels[1][spins[1]]][0], [reels[2][spins[2]]][0]
    if items[0] == items[1] and items[0] == items[2]: return (10 - reel.index(items[0])) * 10
    item = ""; extra = ""
    if items[0] == items[1]: item = items[0]; extra = items[2]
    if items[0] == items[2]: item = items[0]; extra = items[1]
    if items[1] == items[2]: item = items[1]; extra = items[0]
    if item != "":
        num = 10 - reel.index(item)
        if extra == "Wild": num = num * 2
        return num
    return 0

import random
test.describe("Random tests")
reelz = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
for cwtests in range(0,96):
    reel1z = random.sample( reelz, len(reelz) )
    reel2z = random.sample( reelz, len(reelz) )
    reel3z = random.sample( reelz, len(reelz) )
    spinsz = [random.randint(0,len(reelz)-1), random.randint(0,len(reelz)-1), random.randint(0,len(reelz)-1)]
    print("Reel 1 = " + str(reel1z))
    print("Reel 2 = " + str(reel2z))
    print("Reel 3 = " + str(reel3z))
    print("Testing for " + str(spinsz))
    resultz = fruitSolveIt([reel1z,reel2z,reel3z],spinsz)
    print("Expecting result = "+str(resultz))
    test.assert_equals(fruit([reel1z,reel2z,reel3z],spinsz), resultz, "Should return: '"+str(resultz)+"'")