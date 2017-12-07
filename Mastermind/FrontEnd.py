#__author__ = 'zaq92_000'
"""
TODO:
1)End the game more cleanly?
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
#make the display white
gameDisplay.fill(white)
#the flag to exit the game
gameExit = False
#the colors given from the player
colorlist = []
#number complement of the colorlist to compare to theCode
numberlist = []
#the code to decrypt
theCode = []
possible_numbers = range(0, 7)
theCode = random.sample(possible_numbers, 4)
#this is for handling the guess segments being given from the user
#turncount = which subpart of the guess are they inputting
turncount = 0
subcount = 0
number = 0
#print(theCode)


#puts an image in the display
def background(x, y):
    gameDisplay.blit(image, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


#how to change message color?
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


#colors the bottom with answer
def displayAnswer():
    scount = 0
    tcount = 10
    for i in theCode:
        if i == 0:
            color = white
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            scount += 1
        elif i == 1:
            color = red
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            scount += 1
        elif i == 2:
            color = blue
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            scount += 1
        elif i == 3:
            color = yellow
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            scount += 1
        elif i == 4:
            color = green
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            scount += 1
        elif i == 5:
            color = orange
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            scount += 1
        elif i == 6:
            color = purple
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX), box11Y+(tcount*guessboxY), guessboxW, guessboxH])
            scount += 1


#updatepeg(black pegs, white pegs, segment part, turn count)
def updatepeg(bpegs, wpegs, scount, tcount):
    segment = 180
    segpart = 0
    while bpegs > 0:
        color = black
        if segpart == 0:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180), box11Y+(tcount*guessboxY)+(0), 19, 19])
        if segpart == 1:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180+19), box11Y+(tcount*guessboxY)+(0), 19, 19])
        if segpart == 2:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180), box11Y+(tcount*guessboxY)+(19), 19, 19])
        if segpart == 3:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180+19), box11Y+(tcount*guessboxY)+(19), 19, 19])
        bpegs -= 1
        segpart += 1

    while wpegs > 0:
        color = white
        if segpart == 0:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180), box11Y+(tcount*guessboxY)+(0), 19, 19])
        if segpart == 1:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180+19), box11Y+(tcount*guessboxY)+(0), 19, 19])
        if segpart == 2:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180), box11Y+(tcount*guessboxY)+(19), 19, 19])
        if segpart == 3:
            pygame.draw.rect(gameDisplay, color, [box11X+(scount*guessboxX)+(180+19), box11Y+(tcount*guessboxY)+(19), 19, 19])
        wpegs -= 1
        segpart += 1


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
            if tcount < 10:
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


#the board background
background(x, y)
#play game loop
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
                    subcount = 0
                    #set all ticks to 0
                    tickB = 0
                    tickW = 0
                    none = 0
                    remaining_code = []
                    remaining_guess = []
                    if not numberlist:
                        numberlist = [0, 0, 0, 0]
                        i = 0
                        while i < 4:
                            gsegcolor = white
                            updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)
                            subcount += 1
                            i += 1
                        subcount = 0
                    turnflag = True
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
                        message_display("You Won")                  #banner for winning game
                        displayAnswer()
                        updatepeg(tickB, tickW, subcount, turncount)
                        break
                    updatepeg(tickB, tickW, subcount, turncount)
                    turncount += 1
                    updateboard(guessboxW, guessboxH, gsegcolor, bspace, subcount, turncount, turnflag)

                    colorlist.pop()
    else:
        message_display('You Lost')
        displayAnswer()


    pygame.display.update()
pygame.quit()
quit()
