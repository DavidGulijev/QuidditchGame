#-------------------------------------------------------------------------------
# Name:        Quidditch Main
# Purpose:     Game
# Author:      David Gulijev
# Created:     07/12/2020
# Licence:     <David Gulijev>
#-------------------------------------------------------------------------------

#importing the class imports
from arena import Arena
from player import Player
from snitch import Snitch

#adding in the pygame imports, and aswell as initialising the pygame mixer
import random, sys, copy, os, pygame
from pygame.locals import *
from pygame import mixer
pygame.init()
pygame.mixer.init()

#Background music that happens to loop
mixer.music.load('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/background.mp3')
mixer.music.play(-1)

#Setting up the first level enviroment by adding coordinates and loading arena()
arena = Arena()
player1 = Player("^", 10, 2)
player2 = Player("~", 10, 8)
snitch = Snitch("@", 2, 5)

FPS = 30                    #frames per second the game will be run at
WINWIDTH = 1200              #width of the program's window, in pixels
WINHEIGHT = 1000             #height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2) #you need to know 1/2 sizes so you can
HALF_WINHEIGHT = int(WINHEIGHT / 2) #place things centrally

#The total width and height of each tile in pixels.
TILEWIDTH = 32
TILEHEIGHT = 32
TILEFLOORHEIGHT = 32

#setting up some presets up for colours to be called later
BRIGHTBLUE = (127,198,240)
WHITE      = (255, 255, 255)
BLUE = (51, 51, 255)
RED = (255, 0, 0)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

#dictionary of images used for variety of sprites, each one being 32x32px

IMAGESDICT = {'floor': pygame.image.load("Assets/floor.gif"),
              'wall': pygame.image.load("Assets/wall.gif"),
              'snitch': pygame.image.load("Assets/sprout.gif"),
              'player1': pygame.image.load("Assets/player1.gif"),
              'player2': pygame.image.load("Assets/player2.gif"),
              'spacer': pygame.image.load("Assets/spacer.gif")}

TILEMAPPING = { '#':IMAGESDICT['wall'],
                ' ':IMAGESDICT['floor'],
                '@':IMAGESDICT['snitch'],
                '/':IMAGESDICT['spacer'],
                '^':IMAGESDICT['player1'],
                '~':IMAGESDICT['player2']}
#initilises the pygame, and sets up the rest of the enviroment used for the game
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Quidditch v1.0')
BASICFONT = pygame.font.Font('freesansbold.ttf', 40)
level = 1

""" There is alot to explain in class Moveplayer, so I will explain it mostly in here as not to repeat 4 times below for each move.
    So this class puts the move mechanics of the player together. It first calls the x to check if there is anything infront of it that might block it,
    if x finds a block then it will play a sound and print in the shell that the player is blocked, this will stop the player from moving.
    Next, it will do an else if the x hits a snitch, then it will print a message and then play another sound, and also add to the counter.
    Lastly, the most important one, it will then do an else, this will move the player if there is nothing detected and update the coordinates aswell"""

class Moveplayer(object):
    def __init__(self,playerInput):
        self.player = playerInput

    def left(self):
        #moving the player to the left....
        x = arena.getChaplayerPos(self.player.getRow(), self.player.getCol() - 1)
        if x == "#" or x == "^" or x=="~":
            negative_sound = mixer.Sound('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/negative.mp3')
            negative_sound.play()
            print ("You are being blocked")
        else:
            if x == "@":
                print ("You caught the snitch!")
                self.player.eatSnitch()
                arena.eatSnitch()
                click_sound = mixer.Sound ('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/click.mp3')
                click_sound.play()
            arena.cleaplayerPos(self.player.getRow(), self.player.getCol())
            self.player.moveLeft()
            arena.placeplayer(self.player.getChar(), self.player.getRow(), self.player.getCol())
            self.player.countDown()
            print(self.player.counter)
        print (arena.toString())
        print (self.player.toString())

    def right(self):
        #moving the player to the right....
        x = arena.getChaplayerPos(self.player.getRow(), self.player.getCol() + 1)
        if x == "#" or x == "^" or x=="~":
            negative_sound = mixer.Sound('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/negative.mp3')
            negative_sound.play()
            print ("You are being blocked")
        else:
            if x == "@":
                print ("You caught the snitch!")
                self.player.eatSnitch()
                arena.eatSnitch()
                click_sound = mixer.Sound('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/click.mp3')
                click_sound.play()
            arena.cleaplayerPos(self.player.getRow(), self.player.getCol())
            self.player.moveRight()
            arena.placeplayer(self.player.getChar(), self.player.getRow(), self.player.getCol())
            self.player.countDown()
            print(self.player.counter)
        print (arena.toString())
        print (self.player.toString())

    def up(self):
        #moving the player up....
        print(self.player.getRow(), self.player.getCol())
        x = arena.getChaplayerPos(self.player.getRow()-1, self.player.getCol())
        if x == "#" or x == "^" or x=="~":
            negative_sound = mixer.Sound('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/negative.mp3')
            negative_sound.play()
            print ("You are being blocked")
        else:
            if x == "@":
                print ("You caught the snitch!")
                self.player.eatSnitch()
                arena.eatSnitch()
                click_sound = mixer.Sound('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/click.mp3')
                click_sound.play()
            arena.cleaplayerPos(self.player.getRow(), self.player.getCol())
            self.player.moveUp()
            arena.placeplayer(self.player.getChar(), self.player.getRow(), self.player.getCol())
            self.player.countDown()
            print(self.player.counter)
        print (arena.toString())
        print (self.player.toString())

    def down(self):
        #moving the player down....
        print(self.player.getRow(), self.player.getCol())
        x = arena.getChaplayerPos(self.player.getRow()+1, self.player.getCol())
        if x == "#" or x == "^" or x=="~":
            negative_sound = mixer.Sound('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/negative.mp3')
            negative_sound.play()
            print ("You are being blocked")
        else:
            if x == "@":
                print ("You caught the snitch!")
                self.player.eatSnitch()
                arena.eatSnitch()
                click_sound = mixer.Sound('C:/Users/Bob/PycharmProjects/QuidditchV2/Assets/click.mp3')
                click_sound.play()
            arena.cleaplayerPos(self.player.getRow(), self.player.getCol())
            self.player.moveDown()
            arena.placeplayer(self.player.getChar(), self.player.getRow(), self.player.getCol())
            self.player.countDown()
            print(self.player.counter)
        print (arena.toString())
        print (self.player.toString())

"""The class MoveSnitch is very similar to Moveplayer, they both have very similar mechanics, only that it is simplified, and works
with the snitch instead of the player. The class snitch only works to see if there is a wall, there will be no sound, or any fancy
coordinates printed"""
class MoveSnitch(object):
    def __init__(self,snitchInput):
        self.snitch = snitchInput

    def left (self):
        x = arena.getChaplayerPos(self.snitch.getRow(), self.snitch.getCol() -1)
        if x == "#" or x == "^" or x == "~":
            pass
        else:
            arena.cleaplayerPos(self.snitch.getRow(), self.snitch.getCol())
            self.snitch.moveLeft()
            arena.placesnitch(self.snitch.getChar(), self.snitch.getRow(), self.snitch.getCol())

    def right (self):
        x = arena.getChaplayerPos(self.snitch.getRow(), self.snitch.getCol() +1)
        if x == "#" or x == "^" or x == "~":
            pass
        else:
            arena.cleaplayerPos(self.snitch.getRow(), self.snitch.getCol())
            self.snitch.moveRight()
            arena.placesnitch(self.snitch.getChar(), self.snitch.getRow(), self.snitch.getCol())

    def up (self):
        x = arena.getChaplayerPos(self.snitch.getRow() -1,self.snitch.getCol())
        if x == "#" or x == "^" or x == "~":
            pass
        else:
            arena.cleaplayerPos(self.snitch.getRow(), self.snitch.getCol())
            self.snitch.moveUp()
            arena.placesnitch(self.snitch.getChar(), self.snitch.getRow(), self.snitch.getCol())

    def down (self):
        x = arena.getChaplayerPos(self.snitch.getRow() + 1, self.snitch.getCol())
        if x == "#" or x == "^" or x == "~":
            pass
        else:
            arena.cleaplayerPos(self.snitch.getRow(), self.snitch.getCol())
            self.snitch.moveDown()
            arena.placesnitch(self.snitch.getChar(), self.snitch.getRow(), self.snitch.getCol())

#This allows it to share the moves to both players without moving them both, and allows the snitch to have an abbreviation
move = Moveplayer(player1)
move2 = Moveplayer(player2)
move3 = MoveSnitch(snitch)

#This puts everything together allows the game to work properly
def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT, level, player1, player2, snitch, playerText
    #Places the players and snitches into the game
    arena.placeplayer(player1.getChar(), player1.getRow(), player1.getCol())
    arena.placeplayer2(player2.getChar(), player2.getRow(),player2.getCol())
    arena.placesnitch(snitch.getChar(),snitch.getRow(),snitch.getCol())
    print (arena.toString())
    #Draws the arena screen
    drawMap(arena)
    while True:

        """These are the keyboard controls for player 2, he controls the game with the ARROW keys, when the arrow keys are pressed
        then it will call one of the move functions, aswell as one of the snitch move functions, the snitch is delicately set to have
        opposite move functions as it gives the snitch a chance to run away from the players"""
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                # Player clicked the "X" at the corner of the window.
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    move2.right()
                    move3.left()
                elif event.key == K_UP:
                    move2.up()
                    move3.down()
                elif event.key == K_LEFT:
                    move2.left()
                    move3.right()
                elif event.key == K_DOWN:
                    move2.down()
                    move3.up()
                elif event.key == K_SPACE:
                    restart()
                else:
                    pass
            mapNeedsRedraw = True
            """Similar thing is happening here with the player 2 except that he controls the WASD movements instead."""
            if event.type == KEYDOWN:
                if event.key == K_d:
                    move.right()
                    move3.left()
                elif event.key == K_w:
                    move.up()
                    move3.down()
                elif event.key == K_a:
                    move.left()
                    move3.right()
                elif event.key == K_s:
                    move.down()
                    move3.up()
                else:
                    pass
            mapNeedsRedraw = True

            """This will check to see if the level is complete by seeing if the snitch is equal to 0, if he is equal to 0, then 
            the next level will be played, and the players and snitches will be placed into the arena"""
            if (level == 1):
                if (arena.snitch == 0):
                    #level is completed
                    print ("Level 1 completed!")
                    arena.goToLevel2()
                    player1.setRow(11)
                    player1.setCol(1)
                    player2.setRow(11)
                    player2.setCol(9)
                    snitch.setRow(2)
                    snitch.setCol(5)
                    arena.placeplayer("^",11,1)
                    arena.placeplayer2("~",11,9)
                    arena.placesnitch("@",2,5)
                    level = 2
            if (level == 2):
                if (arena.snitch == 0):
                    # level is completed
                    print("Level 2 completed!")
                    arena.goToLevel3()
                    player1.setRow(13)
                    player1.setCol(1)
                    player2.setRow(13)
                    player2.setCol(9)
                    snitch.setRow(2)
                    snitch.setCol(5)
                    arena.placeplayer("^", 13, 1)
                    arena.placeplayer2("~", 13, 9)
                    arena.placesnitch("@",2,5)
                    level = 3
            if (level == 3):
                if (arena.snitch == 0):
                    # level is completed
                    print("Level 3 completed!")
                    arena.goToLevel4()
                    player1.setRow(16)
                    player1.setCol(1)
                    player2.setRow(16)
                    player2.setCol(9)
                    snitch.setRow(2)
                    snitch.setCol(5)
                    arena.placeplayer("^", 16, 1)
                    arena.placeplayer2("~", 16, 9)
                    arena.placesnitch("@",2,5)
                    level = 4
            #if the level is equal to 4 and snitch equal to 0 the game will print a message and exit the game.
            if (level ==4):
                if (arena.snitch ==0):
                    print("The game is complete")
                    sys.exit()


        #thread 2: redraws the screen
        DISPLAYSURF.fill(BGCOLOR) #draws the turquoise background
        #if something has changed, redraw....
        if mapNeedsRedraw:
            mapSurf = drawMap(arena)
            mapNeedsRedraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        # Draw the map on the DISPLAYSURF object.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        """This is where the game's score is being held, the score uses the counters set earlier, and the colour and font presets
        to be used here, the coordinates sets the text position"""
        playerText = BASICFONT.render("Moves : " + str(player1.counter), True, RED)
        DISPLAYSURF.blit(playerText, (50, 800))
        playerText = BASICFONT.render("Moves : " + str(player2.counter), True, BLUE)
        DISPLAYSURF.blit(playerText, (900, 800))
        playerText = BASICFONT.render("Snitches : " + str(player1.snitch), True, RED)
        DISPLAYSURF.blit(playerText, (50, 100))
        playerText = BASICFONT.render("Snitches : " + str(player2.snitch), True, BLUE)
        DISPLAYSURF.blit(playerText, (900, 100))

        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

def drawMap(arena):
    #draw the tile sprites onto this surface.
    #this creates the visual map!
    mapSurfWidth = arena.getWidth() * TILEWIDTH
    mapSurfHeight = arena.getHeight() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)
    for h in range(arena.getHeight()):
        for w in range(arena.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if arena.getChaplayerPos(h, w) in TILEMAPPING:
                #checks in the TILEMAPPING directory above to see if there is a
                #matching picture, then renders it
                baseTile = TILEMAPPING[arena.getChaplayerPos(h,w)]

            # Draw the tiles for the map.
            mapSurf.blit(baseTile, thisTile)
    return mapSurf

"""Just a basic restart function that restarts and redraws the game, it has its problems 
but it works fine when wanting to move back to level 1"""
def restart():
    arena.__init__()
    player1.setRow(10)
    player1.playerRestart()
    player1.setCol(2)
    player1.snitchRestart()
    player2.setRow(10)
    player2.setCol(8)
    player2.playerRestart()
    player2.snitchRestart()
    snitch.setRow(2)
    snitch.setCol(5)
    arena.placeplayer(player1.getChar(), player1.getRow(), player1.getCol())
    arena.placeplayer2(player2.getChar(), player2.getRow(), player2.getCol())
    arena.placesnitch(snitch.getChar(),snitch.getRow(),snitch.getCol())
    drawMap(arena)

#terminates the game
def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
