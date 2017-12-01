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
        ii. Put guess colors into a list inorder to subpartition, respectively
"""
import pygame
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
#t-l pixel of left most answer box
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
pygame.display.set_caption('Caption')       #display window caption
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


#puts an image in the display
def background(x, y):
    gameDisplay.blit(image, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


#Displays text to the screen
def winMessage():
    message_display('You WIN!')


#updateboard(x, y, w, h, color
def updateboard(guessboxX, guessboxY, guessboxW, guessboxH, color):
    #draws the color guess over the corresponding box
    #pygame.draw.rect(where or what object, color, locations[x, y, w, h])
    pygame.draw.rect(gameDisplay, color, [guessboxX, guessboxY, guessboxW, guessboxH])
    list = []
    print("len", len(list))
    if len(list) < 4:
        list.append(color)
    for i in list:
        print("list", i)


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


    #this is for handling the guess segments being given from the user
    #segment counter = which subpart of the guess are they inputting
    background(x, y)
    segcounter = 1
    turncount = 1
    if turncount < 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                background(x, y)
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    gsegcolor = white
                    updateboard(box11X, box11Y, guessboxW, guessboxH, gsegcolor)
                    segcounter += 1
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    gsegcolor = red
                    updateboard(box11X, box11Y, guessboxW, guessboxH, gsegcolor)
                    segcounter += 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    gsegcolor = blue

                    segcounter += 1
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    gsegcolor = yellow

                    segcounter += 1
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    gsegcolor = green

                    segcounter += 1
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    gsegcolor = orange

                    segcounter += 1
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    gsegcolor = purple

                    segcounter += 1
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE or event.key == pygame.K_LEFT:
                    gsegcolor = white

                    segcounter -= 1
                print(event)
                print(gsegcolor)

    else:
        print("display answer")

    pygame.display.update()
pygame.quit()
quit()


########################################################################################################################
#if __name__ == '__main__':
#    main()
