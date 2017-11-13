#__author__ = 'zaq92_000'
import pygame
pygame.init()

#display attributes
display_width = 350
display_height = 600

#Color section
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

#display actual
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Caption')       #display window caption
clock = pygame.time.Clock()                 #clock for something
image = pygame.image.load('board.jpg')     #image to be displayed
imagewidth = 307
imageheight = 545

#image placement(based on it's top-left/origin pixel)
x = 1
y = 1
print(x,y)
#max/min x/y values the image can go with respect to the size of the images size
xMax = display_width - imagewidth       #397 for pewpew
yMax = display_height - imageheight     #332 for pewpew

x_change = 0
y_change = 0
car_speed = 0
gameExit = False


#puts an image in the display
def pewpew(x, y):
    gameDisplay.blit(image, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


#Displays text to the screen
def winMessage():
    message_display('You WIN!')

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        #key catching for moving stuff/needs to become mouse reading
        #KEYDOWN is for pressing down on the key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
        #KEYUP is for releasing a pressed key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0

    x += x_change
    y += y_change

    gameDisplay.fill(white)        #displays a background color
    #image boundary catcher
    if x > xMax:
        x = xMax - 1
        winMessage()
    elif x < 0:
        x = 1
        winMessage()
    elif y > yMax:
        y = yMax - 1
        winMessage()
    elif y < 0:
        y = 1
        winMessage()

    pewpew(x, y)




    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()


########################################################################################################################
#if __name__ == '__main__':
#    main()
