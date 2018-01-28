"""
Introduction
A multi-storey car park (also called a parking garage, parking structure, parking ramp, parkade, parking building, parking deck or indoor parking) is a building designed for car parking and where there are a number of floors or levels on which parking takes place. It is essentially an indoor, stacked car park. Parking structures may be heated if they are enclosed. Design of parking structures can add considerable cost for planning new developments, and can be mandated by cities or states in new building parking requirements. Some cities such as London have abolished previously enacted minimum parking requirements (Source Wikipedia)

Task
Your task is to escape from the carpark using only the staircases provided to reach the exit. You may not jump over the edge of the levels (you’re not Superman!) and the exit is always on the far right of the ground floor.
Rules
1. You are passed the carpark data as an argument into the function.
2. Free carparking spaces are represented by a 0
3. Staircases are represented by a 1
4. Your parking place (start position) is represented by a 2
5. The exit is always the far right element of the ground floor.
6. You must use the staircases to go down a level.
7. You will never start on a staircase.
8. The start level may be any level of the car park.
Returns
Return an array of the quickest route out of the carpark
R1 = Move Right one parking space.
L1 = Move Left one parking space.
D1 = Move Down one level.
Example
Initialise
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
Working Out
You start in the most far right position on level 1
You have to move Left 4 places to reach the staircase => "L4"
You then go down one flight of stairs => "D1"
To escape you have to move Right 4 places => "R4"
Result
result = ["L4", "D1", "R4"]
Good luck and enjoy!


"""




def escape(carpark):

    total_floors = len(carpark)
    total_places = len(carpark[0])
    for i in range(total_floors):
        if 2 in carpark[i]:
            floor = i
            break
    pos = carpark[floor].index(2)
    result = []
    down = 0
    
    while floor != total_floors - 1:
        stairs = carpark[floor].index(1)
        if pos > stairs:
            result.append('L' + str(pos - stairs))
            pos = stairs
        elif pos < stairs:
            result.append('R' + str(stairs - pos))
            pos = stairs
        else:
            down += 1
            floor += 1
        if down > 0 and carpark[floor][pos] != 1:
            result.append('D' + str(down))
            down = 0

    if pos != total_places - 1:
        result.append('R' + str(total_places - 1 - pos))

    return result









def escape(carpark):

    while 2 not in carpark[0]: carpark.pop(0)
    r, ground, pos = [], len(carpark) - 1, carpark[0].index(2)
    for f, floor in enumerate(carpark):
        stairs = floor.index(1) if f != ground else len(floor) - 1
        if stairs != pos:
            r, pos = r + ['RL'[stairs < pos] + str(abs(pos - stairs))], stairs
        if f != ground:
            r += [('D' + str(int(r.pop()[1:]) +1)) if 'D' in r[-1] else 'D1']
    return r

















test.describe("Basic Tests")
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
result = ["L4", "D1", "R4"]
test.it("Expected '"+str(result)+"'")
test.assert_equals(escape(carpark), result)
carpark = [[2, 0, 0, 1, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]
result = ["R3", "D2", "R1"]
test.it("Expected '"+str(result)+"'")
test.assert_equals(escape(carpark), result)
carpark = [[0, 2, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]
result = ["R3", "D3"]
test.it("Expected '"+str(result)+"'")
test.assert_equals(escape(carpark), result)
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]
result = ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]
test.it("Expected '"+str(result)+"'")
test.assert_equals(escape(carpark), result)
carpark = [[0, 0, 0, 0, 2]]
result = []
test.it("Expected '"+str(result)+"'")
test.assert_equals(escape(carpark), result)
import random
test.describe("Random Tests")
def escapeSOLVEIT(carpark):
    result = []
    level = 0; space = 0
    for i in range(0,len(carpark)):
        for a in range(0,len(carpark[i])):
            if carpark[i][a] == 2:
                level = i
                space = a

    while (True):
        if level == len(carpark) - 1:
            if space != len(carpark[0]) - 1:
                result.append("R"+str(len(carpark[0])-space-1))
            space = len(carpark[0]) - 1
        else:
            if carpark[level][space] == 1:
                count = 0
                while (carpark[level][space] == 1 and level != len(carpark)):
                    level += 1
                    count += 1
                result.append("D"+str(count))
            else:
                pos = carpark[level].index(1)
                if pos < space:
                    d = "L"
                else:
                    d = "R"
                result.append(d+str(abs(pos-space)))
                space = pos
        if (space == len(carpark[0]) - 1 and level == len(carpark) - 1): break
    return result
def carparkmaker():
    spaces = random.randint(2,200)
    levels = random.randint(1,200)
    carpark = []
    for l in range(0,levels):
        temp = []
        for s in range(0,spaces):
            temp.append(0)
        carpark.append(temp)
    for l in range(0,levels-1):
        carpark[l][random.randint(0,spaces-1)] = 1
    done = False
    while(not done):
        s = random.randint(0,spaces-1)
        l = random.randint(0,levels-1)
        if carpark[l][s] == 0:
            carpark[l][s] = 2
            done = True
    return carpark

for cwtests in range(0,95):
    carpark = carparkmaker()
    test.assert_equals(escape(carpark), escapeSOLVEIT(carpark))