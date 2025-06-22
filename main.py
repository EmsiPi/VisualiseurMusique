import pygame
from pathlib import Path
import numpy as np

COLOR = (50, 0, 20)
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
text_surface = my_font.render(Path(dir).stem, True, COLOR)
screen.blit(text_surface, (70,100))
# potiCercle = pygame.draw.circle(screen, COLOR, center, 10)
pygame.display.set_caption('GroovingEnPleineLiberté') #Nom de la fenêtre 


pygame.mixer.init() #mixer de musique
my_sound = pygame.mixer.Sound('SquareASaw-Lover.mp3')
my_sound.play() #play le fichier mp3
my_sound.set_volume(0.2)
pygame.display.flip()


# x and y coordinates of the circle center
x=np.linspace(300,800,500)
y=x

# initialize the frame index i 
i=0

while (i<len(x)):
     # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
    
    # fill the surface with the background color -black 
    # this is used to erase the previous frame
    # if you do not call this the circles from the previous 
    # frames will be kept
            
    # draw the circle 
    pygame.draw.circle(screen,
                       COLOR,
                       (int(x[i]),int(y[i])),
                       3)
    
    # update the screen
    pygame.display.flip()
    # introduce a delay
    pygame.time.delay(10)
    # this is used to limite the runtime
    # by using for example 
    # clock.tick(50) once per frame, 
    # the script will not run faster than 50 frames per second.
    clock.tick(50)
    i=i+1

pygame.quit()
