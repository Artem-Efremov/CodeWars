"""
Introduction
  	Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls. Doing so will kill you instantly!
 
Maze Runner
Task
  	You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, you should return Dead. If you find yourself still in the maze after using all the moves, you should return Lost.
 

The Maze array will look like

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

..with the following key
  	0 = Safe place to walk
1 = Wall
2 = Start Point
3 = Finish Point
 

  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"

Rules
  	1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.
2. The start and finish positions will change for the final tests.
3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.
 

Good luck, and stay safe!

"""



def maze_runner(maze, directions):
    
    # 1. Initialization
    
    height_lab = len(maze)
    width_lab = len(maze[0])
    
    for i in range(height_lab):      # Find start
        if 2 in maze[i]:
            j = maze[i].index(2)
            start = [i, j]
    
    direct_table = {'N': [-1, 0], 'E': [0, 1],      # North is the top of list - index decrease
                    'W': [0, -1], 'S': [1, 0]}      # South is the end of list - index increase
    
    # 2. Walk
    
    position = start[:]             # Copy values
     
    for i in directions:
        position[0] += direct_table[i][0]
        position[1] += direct_table[i][1]
        
        if (position[0] not in range(height_lab) or
                    position[1] not in range(width_lab) or
                    maze[position[0]][position[1]] == 1):
            result = 'Dead'
            break
        elif maze[position[0]][position[1]] == 3:
            result = 'Finish'
            break
    else:
        result = 'Lost'
    
    return result









import random
test.describe("Random tests")

maze = [[1,1,1,1,1,1,1,1,0,1],
        [1,3,1,0,1,0,0,0,0,1],
        [1,0,1,0,0,0,1,1,0,1],
        [1,0,1,1,1,1,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,1],
        [1,0,1,0,1,0,1,0,0,1],
        [1,0,1,0,1,0,0,0,0,0],
        [1,0,1,0,1,0,1,1,0,1],
        [1,0,0,0,1,0,0,0,0,1],
        [1,1,1,0,1,1,1,1,2,1]]
        
test.describe("Example tests")

test.it("Should return Finish")
test.assert_equals(maze_runner(maze,["N","N","N","W","W","W","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N"]), "Finish", "Should return Finish")
test.it("Should return Lost")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","N","N","N","W","W","W","S","W","W","N"]), "Lost")
test.it("Should return Dead")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","S","S","S","S","S","S"]), "Dead")
test.it("Should return Dead")
test.assert_equals(maze_runner(maze,["N","W","W","W","W"]), "Dead")
test.it("Should return Lost")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","N","N","N","N","S","S","S","S","S","S","S","S","S"]), "Lost")
test.it("Should return Dead")
test.assert_equals(maze_runner(maze,["N","E","E"]), "Dead")
test.it("Should return Finish")
test.assert_equals(maze_runner(maze,["N","W","W","W","N","N","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N","S","S"]), "Finish")
test.it("Should return Lost")
test.assert_equals(maze_runner(maze,["N","W","W","W","N","N"]), "Lost")
test.it("Should return Lost")
test.assert_equals(maze_runner(maze,["N","N","N","E"]), "Lost")
test.it("Should return Dead")
test.assert_equals(maze_runner(maze,["N","N","N","W","W","W","N","N","W","W","S","S","S","S","S","S"]), "Dead")
test.it("Should return Finish")
test.assert_equals(maze_runner(maze,["N","W","W","W","N","N","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N"]), "Finish")

def maze_runner2(maze, directions):
    startX = 0 ; startY = 0
    for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[x][y] == 2:
                startX = y
                startY = x

    for dire in directions:
        if dire == "N": startY = startY - 1
        if dire == "E": startX = startX + 1
        if dire == "S": startY = startY + 1
        if dire == "W": startX = startX -1
        if startY < 0 or startY > len(maze)-1 or startX < 0 or startX > len(maze)-1 or maze[startY][startX] == 1: return "Dead"
        if maze[startY][startX] == 3: return "Finish"

    return "Lost"

for rtest in range(139):
    maze = []
    l = random.randint(5, 7)
    for z in range(l):
        t = []
        t.extend([0] * l)
        maze.extend([t])
    w = random.randint(1, l*l-10)
    for z in range(w):
        x = random.randint(0,l-1)
        y = random.randint(0,l-1)
        maze[x][y] = 1
    x = random.randint(0,l-1)
    y = random.randint(0,l-1)
    maze[x][y] = 3
    x = random.randint(0,l-1)
    y = random.randint(0,l-1)
    maze[x][y] = 2

    directions = []
    m = random.randint(1,60)
    for x in range(0,m):
        d = random.randint(0,4)
        if d == 0: directions.extend("N")
        if d == 1: directions.extend("E")
        if d == 2: directions.extend("S")
        if d == 3: directions.extend("W")
    
    solution = maze_runner2(maze, directions)
    test.it("Should return "+solution)
    test.assert_equals(maze_runner(maze,directions), solution)
