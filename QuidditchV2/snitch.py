#-------------------------------------------------------------------------------
# Name:        Quidditch Snitch
# Purpose:     Game
# Author:      David Gulijev
# Created:     14/01/2021
# Licence:     <David Gulijev>
#-------------------------------------------------------------------------------

"""Class snitch uses almost all the same functions as the Player class, with the exception of not printing out any of the
coordinates, and aswell as not having any of the restart functions. Refer to player class for details"""

class Snitch:
    def __init__(self, x, r, c):
        self.char = x
        self.row = r
        self.col = c

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getChar(self):
        return self.char

    def getsnitch(self):
        return self.snitch

    def setRow(self, r):
        self.row = r

    def setCol(self, c):
        self.col = c

    def moveRight(self):
        self.col += 1

    def moveLeft(self):
        self.col -= 1

    def moveUp(self):
        self.row -=1

    def moveDown(self):
        self.row +=1
