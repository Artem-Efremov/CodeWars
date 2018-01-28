"""
https://www.codewars.com/kata/5a34c8ce55519ecb15000012/train/python



In traditional American checkers (also known as draughts outside the U.S.), when one of your pieces becomes a king, it gains the advantage of being able to move diagonally in any direction. This adds more possibilities with regard to capturing multiple enemy pieces in a single turn.

In this kata you are presented with an n x n board. While your opponent has several pieces on the board, you have only one remaining piece — a king. Using the same mechanics as in American checkers, your goal is to capture the maximum number of enemy pieces in the next move with your king.

Input
Your function will receive an array of length n comprised of strings of length n. Each string value represents each row of the board, from top to bottom.

Each string will consist of one or more of the following:
" ": an unoccupied cell denoted by a space character
X: a cell occupied by an enemy piece
K: the location of your king piece
Output
Your function should return the maximum number of enemy pieces that can be captured in one turn.
Test Example
board = [
    '       X',
    '        ',
    ' X X X  ',
    '        ',
    ' X X X  ',
    '        ',
    '   X X  ',
    '    K   '
]
king_move_combo(board) #7
Below (left) is a graphic representation of the example board and (right) a set of moves to obtain the solution.

Checkerboard image at https://i.imgur.com/KAs4tIZ.png
Technical Details
Input will always be valid.
Board size range: 16 >= n >= 8
If you enjoyed this kata, be sure to check out my other katas.


https://www.codewars.com/users/docgunthrop/authored

"""

