#-------------------------------------------------------------------------------
# Name:        Quidditch arena
# Purpose:     Game
# Author:      David Gulijev
# Created:     07/12/2020
# Licence:     <David Gulijev>
#-------------------------------------------------------------------------------

class Arena:
    """ A 2D arena. """
    def __init__(self):
        """the arena constructor"""
        """arena 1 (level 1) is set to have a smaller size as it's the first level in the game,it has width of 11 and height of 13
        The '#' Will act likes walls and '/' will act like spacers"""
        self.arena = [['#','#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.snitch = 1
        self.width = 11
        self.height = 13


    def toString(self):
        """prints out the arena
	(none) -> none"""
        printme = ""
        for i in range (0,len(self.arena)):
            for j in self.arena[i]:
                printme = printme + j
            printme = printme + "\n"
        return printme

    #Places player1 into the arena
    def placeplayer(self, player_char, row, column):
        self.arena[row][column] = player_char

    #Places player2 into the arena
    def placeplayer2(self, player_char2, row, column):
        self.arena[row][column] = player_char2

    #Places the snitch into the arena
    def placesnitch(self, snitch, row, column):
        self.arena[row][column] = snitch

    #Clears a position
    def cleaplayerPos(self, row, col):
        self.arena[row][col] = " "

    """This checks for walls without actually moving any of the players or snitches, it's good because It allows you
    to check whats infront of you without taking any action"""
    def getChaplayerPos(self, row, col):
        return self.arena[row][col]

    #This will add towards the caught snitches counter
    def eatSnitch(self):
        self.snitch -= 1

    #This is the 2nd arena, this one is slightly more harder because there is more obstacles
    def goToLevel2(self):
        self.arena = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                     ['#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
                     ['#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', '#', '#', '/', '#', '#', ' ', ' ', '#'],
                     ['#', ' ', '#', '#', '/', '/', '/', '#', '#', ' ', '#'],
                     ['#', '#', '#', '/', '/', '/', '/', '/', '#', '#', '#']]
        self.snitch = 1
        self.width = 11
        self.height = 13

    #This will return the width
    def getWidth(self):
        return self.width

    #This will return the height
    def getHeight(self):
        return self.height

    #This is the 3rd arena, this is bigger and size, and has even more obstacles than the 2nd
    def goToLevel3(self):
        self.arena = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                     ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                     ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#'],
                     ['/', '/', '/', '#', ' ', '#', ' ', '#', '/', '/', '/'],
                     ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#'],
                     ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
                     ['#', ' ', '#', '/', '/', '/', '/', '/', '#', ' ', '#'],
                     ['#', '#', '#', '/', '/', '/', '/', '/', '#', '#', '#']]
        self.snitch = 1
        self.width = 11
        self.height = 15

    """This is the final arena level, this is to have the largest size, and to have the most obstacles, each level so far
    has been an increase in difficulty"""
    def goToLevel4(self):
        self.arena = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                      ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                      ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                      ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                      ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                      ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
                      ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                      ['#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
                      ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                      ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
                      ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                      ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#'],
                      ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                      ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
                      ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                      ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#'],
                      ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                      ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        # maze 1 (level 1) is set to have a snitch, and a screen width of 11 and height of 13
        self.snitch = 1
        self.width = 11
        self.height = 18

    #Simply returns the current arena being played
    def getCurrentarena(self):
        return self.arena
