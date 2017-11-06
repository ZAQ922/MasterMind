#__author__ = 'zaq92_000'
import pygame
pygame.init()

#display attributes
display_width = 800
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
image = pygame.image.load('pewpew.jpg')     #image to be displayed

#image placement(based on it's top-left/origin pixel)
x = (display_width / 4)
y = (display_height / 4)
crashed = False

#puts an image in the display
def pewpew(x, y):
    gameDisplay.blit(image, (x, y))


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    #gameDisplay.fill(white)        #display background color
    pewpew(x, y)                    #calls out to image input fx
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()


########################################################################################################################
#if __name__ == '__main__':
#    main()
