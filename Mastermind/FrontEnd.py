#__author__ = 'zaq92_000'
"""
TODO:
1)Decide how the player should input their guess
    B. input corresponding numbers in a L>R order
2)Need a backspace/delete function to fix mistakes before submitting guess
    A. This needs to replace the square with something like the same background
        or just greying it out?
3)Need a submit button or on 'ENTER' or both
    A.Ensure that only the proper row can have guesses submitted on it
        i. Will only change row after "ENTER/SUBMIT" were hit
"""
import pygame
import random
pygame.init()

#display attributes
display_width = 308
display_height = 546
#each box is exactly 38x38 pixels (
#REMINDER: 2 pixels between each box + 1 for next boxes pixel position = +3 to calculations
guessboxW = 38
guessboxH = 38
extrapixels = 3
#Some kinda offset made the first box's position 40x40
guessboxX = 40
guessboxY = 40
#top-left pixel position of top-left box
box11X = 50
box11Y = 20
#top-left pixel position of top score box
pegboxX = 230
pegboxY = 20
#top-left pixel of left most answer box
answerboxX = 50
answerboxY = 420

#Color section
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
orange = (255, 165, 0)
purple = (160, 32, 240)
#default segment color
gsegcolor = black
#display actual
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mastermind')    #display window caption
clock = pygame.time.Clock()                 #clock for something
image = pygame.image.load('board.jpg')      #image to be displayed
imagewidth = 307#307
imageheight = 545#545

#image placement(based on it's top-left/origin pixel)
x = 0
y = 0

#max/min x/y values the image can go with respect to the size of the images size
xMax = display_width - imagewidth
yMax = display_height - imageheight

#x changes 4 times per guess
#y changes 1 time per guess
x_change = 0
y_change = 0
gameDisplay.fill(white)
gameExit = False
colorlist = []
numberlist = []

#make the code to decrypt
theCode = []
possible_numbers = range(1, 7)
theCode = random.sample(possible_numbers, 4)


#this is for handling the guess segments being given from the user
#turncount = which subpart of the guess are they inputting
turncount = 0
subcount = 0
number = 0


#puts an image in the display
def background(x, y):
    gameDisplay.blit(image, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


#Displays text to the screen
def winMessage():
    message_display('You WIN!')


def lossMessage():
    message_display('FUC')


#updateboard(x, y, w, h, color, backspace)
def updateboard(guessboxW, guessboxH, color, bspace, scount, tcount, tflag):
    #if not backspace pressed
    if not bspace:
        #turn/enter flag
        if tflag:
            while len(colorlist) > 0:
                colorlist.pop()
            while len(numberlist) > 0:
                numberlist.pop()
            color = black
            tflag = False
        #0-6 input to numberlist
        if len(colorlist) < 4:
            colorlist.append(color)
            #draws the color guess over the corresponding box
            #pygame.draw.rect(where or what object, color, locations[x, y, w, h]) math for dynamic drawing
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            if color == white:
                numberlist.append(0)
            elif color == red:
                numberlist.append(1)
            elif color == blue:
                numberlist.append(2)
            elif color == yellow:
                numberlist.append(3)
            elif color == green:
                numberlist.append(4)
            elif color == orange:
                numberlist.append(5)
            elif color == purple:
                numberlist.append(6)
    else:
        if len(colorlist) > 0:
            colorlist.pop()
            numberlist.pop()
            if scount < 0:
                scount = 0
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(turncount*guessboxY), guessboxW, guessboxH])

background(x, y)
while not gameExit:
    bspace = False
    turnflag = False
    if turncount < 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if subcount <= 0:
                subcount = 0
            elif subcount >= 4:
                subcount = 4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    gsegcolor = white
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    subcount += 1
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    gsegcolor = red
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    subcount += 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    gsegcolor = blue
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    subcount += 1
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    gsegcolor = yellow
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    subcount += 1
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    gsegcolor = green
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    subcount += 1
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    gsegcolor = orange
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    subcount += 1
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    gsegcolor = purple
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    subcount += 1
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE or event.key == pygame.K_LEFT:
                    gsegcolor = black
                    bspace = True
                    subcount -= 1
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                elif event.key == pygame.K_KP_ENTER:
                    turnflag = True
                    subcount = 0
                    #set all ticks to 0
                    tickB = 0
                    tickW = 0
                    none = 0
                    remaining_code = []
                    remaining_guess = []
                    for guess, part in zip(numberlist, theCode):  #index and part of the enumerated guess
                        if guess == part:                #if it equals the code at this index
                            tickB += 1
                        else:
                            remaining_code.append(part)  #whatever is left, see if it gets a tickW
                            remaining_guess.append(guess)
                    for guess in remaining_guess:       #cycle through the remaining guesses
                        if guess in remaining_code:     #if it's in there, it gets tickW
                            tickW += 1
                        #   remaining_code.remove(guess)#can replace the "none += 1"
                        else:                           #else it doesn't and should be blank
                            none += 1
                    if tickB == 4:                                  #when you get 4 black ticks you win
                        endgame = True                              #for ending the game once you've won
                        winMessage()                                #banner for winning game
                        gameExit = True
                    else:                                           #otherwise output ticks to help them solve it
                        print("code:", theCode)
                        print("Black:", tickB)                      #banner for mid-game
                        print("White:", tickW)
                        print("None:", none)
                    turncount += 1
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                    colorlist.pop()

    else:
        lossMessage()
        gameExit = True

    pygame.display.update()
pygame.quit()
quit()


########################################################################################################################
#if __name__ == '__main__':
#    main()
