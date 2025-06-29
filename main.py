import random
import pygame
from pathlib import Path
import numpy as np

Pourpre = (50, 0, 20)
Violet = (160,32, 240)
Jaune = (255, 100, 20)
Magenta = (0, 255, 255)
Vert = (0,255,0)
Couleurs = [Pourpre, Violet, Jaune, Magenta,Vert]

(width, height) = (400, 400)
center = (200,200)
screen = pygame.display.set_mode((width, height))

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
background_colour = (200,200,250)
screen.fill(background_colour)
dir = 'SquareASaw-Lover.mp3'
text_surface = my_font.render(Path(dir).stem, True, Pourpre)
screen.blit(text_surface, (70,100))
#potiCercle = pygame.draw.circle(screen, COLOR, center, 10)
pygame.display.set_caption('GroovingEnPleineLiberté') #Nom de la fenêtre 


pygame.mixer.init() #mixer de musique
my_sound = pygame.mixer.Sound('SquareASaw-Lover.mp3')
my_sound.play() #play le fichier mp3
my_sound.set_volume(0.2)
pygame.display.flip()


# x and y coordinates of the circle center
x=np.linspace(300,800,500)
y=x

c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)

# initialize the frame index i 
i=0
breeze = 1

running = True
while (running):
     # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw the circle 
    for r in range (1,20):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        if(c1 % 255 == 0):
            if(c1==255):
                breeze = breeze*-1
            else:
                breeze = 1
        

        c1 = c1 + breeze

        print(c1)
        # if 0<=c1<255:
            #c1 += 1
            #print(c1)
        #elif c1==255:
        #     c1 -= 255
        # elif c1 < 0:
        #     c1 = 0
        pygame.draw.circle(screen,
                       (c1,c2,c3),
                       center,
                       r)
        pygame.display.flip()
        pygame.time.delay(30)
        screen.fill(background_colour)
        text_surface = my_font.render(Path(dir).stem, True, Pourpre)
        screen.blit(text_surface, (70, 100))

    
    if (i == 4):
        i = 0
    

    # this is used to limite the runtime
    # by using for example 
    # clock.tick(50) once per frame, 
    # the script will not run faster than 50 frames per second.
    clock.tick(50)
    i=i+1

pygame.quit()
