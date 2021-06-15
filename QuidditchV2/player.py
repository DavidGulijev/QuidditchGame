#-------------------------------------------------------------------------------
# Name:        Quidditch Player
# Purpose:     Game
# Author:      David Gulijev
# Created:     07/12/2020
# Licence:     <David Gulijev>
#-------------------------------------------------------------------------------

class Player:
    def __init__(self, x, r, c):
        """constructor for the player.  Needs to pass in values
       for the character representing the player, the row and the column
       £>>>player("$", 2, 3)
       Nonetype"""
        self.char = x
        self.row = r
        self.col = c
        self.snitch = 0
        self.counter = 0

    #adds the coordinate message to the shell
    def toString(self):
        info = "player " + self.char + " at row " + str(self.row) + " and column " + str(self.col)
        info = info +  " has caught " + str(self.snitch) + " snitch(es) today."
        return info

    #returns with the current row
    def getRow(self):
        return self.row

    #returns the current column
    def getCol(self):
        return self.col

    #returns the current character
    def getChar(self):
        return self.char

    #sets the row
    def setRow(self, r):
        self.row = r

    #sets the column
    def setCol(self, c):
        self.col = c

    #moves right by adding to column
    def moveRight(self):
        self.col += 1

    #moves left by subtracting to column
    def moveLeft(self):
        self.col -= 1

    #moves up by subtracting to row
    def moveUp(self):
        self.row -=1

    #moves down by adding to row
    def moveDown(self):
        self.row +=1

    #adds +1 to the snitch score
    def eatSnitch(self):
        self.snitch += 1

    #adds to the movement score
    def countDown(self):
        self.counter += 1

    #resets the counter to 0
    def playerRestart(self):
        self.counter = 0

    #resets the snitch score to 0
    def snitchRestart(self):
        self.snitch = 0