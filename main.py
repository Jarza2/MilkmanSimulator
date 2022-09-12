#You need to pip/pip3 import pygame, screeninfo
from operator import contains
import pygame, sys, shelve
from screeninfo import *
for m in get_monitors():
    print(str(m))
pygame.init()

#Images
grass = pygame.image.load('images/grass.png')
dirt = pygame.image.load('images/dirt.png')
gameicon = pygame.image.load('images/milk.png')
skybox = pygame.image.load('images/skybox.png')
skyboxrect = skybox.get_rect()

#Pygame initialization process
size = width, height = m.width, m.height
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Milkman Simulator')
pygame.display.toggle_fullscreen()
pygame.display.set_icon(gameicon)
game = True

shelfFile = shelve.open('savefile')
shelfFile.close()

#Keybind values
quit_bind = pygame.K_ESCAPE

while game: #Infinite loop a.k.a. main game loop.

 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit
        sys.exit()

    if pygame.key.get_focused(): #Detects key inputs (Outputs true if key input)
            if pygame.key.get_pressed() [quit_bind]: #Detects is ESC is pressed, therefore closing the program
                print('Program closed by user hitting exit key')
                pygame.quit()
                sys.exit()
    
    screen.blit(skybox, skyboxrect)
    pygame.transform.scale(skybox, (m.width, m.height))
    pygame.display.flip()