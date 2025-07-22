import random
import pygame
import math
import sys
from pathlib import Path
import numpy as np
import librosa

pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
Pourpre = (50, 0, 20)
Violet = (160,32, 240)
Jaune = (255, 100, 20)
Magenta = (0, 255, 255)
Vert = (0,255,0)
Couleurs = [Pourpre, Violet, Jaune, Magenta,Vert]

(width, height) = (400, 400)
center = (200,200)
screen = pygame.display.set_mode((width, height))


my_font = pygame.font.SysFont('Comic Sans MS', 30)
image_bouton = pygame.image.load('arrow.png').convert_alpha()
image_bouton_rect = image_bouton.get_rect()
clock = pygame.time.Clock()


time = 0
background_colour = (200,200,250)
screen.fill(background_colour)
dir = 'SquareASaw-Lover.mp3'
text_surface = my_font.render(Path(dir).stem, True, Pourpre)
screen.blit(text_surface, (70,100))
#potiCercle = pygame.draw.circle(screen, COLOR, center, 10)
y, sr = librosa.load('SquareASaw-Lover.mp3')
from librosa.beat import beat_track
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
tempo = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)
print(tempo)

pygame.display.set_caption('GroovingEnPleineLiberté') #Nom de la fenêtre 


pygame.mixer.init() #mixer de musique
my_sound = pygame.mixer.Sound('SquareASaw-Lover.mp3')
my_sound.play() #play le fichier mp3
my_sound.set_volume(0.2)
pygame.display.flip()

R = 255
G = 138
B = 138 
rgb = [R,G,B]
x = 0
running = True
while (running):
     # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw the circle 
    if (x <= 40):
        x=x+1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        #Définition des valeurs RGB, degradé à l'aide d'une fonction sinusoïdale
        r = int((math.sin(time) + 1) * 127.5)
        g = int((math.sin(time + 2) + 1) * 127.5)
        b = int((math.sin(time + 4) + 1) * 127.5)
        pygame.draw.circle(screen,
                       (r,g,b),
                       (200,200),
                       (math.sin(time) + 1)* 127.5),
        pygame.display.flip()
        pygame.time.delay(30)
        screen.fill(background_colour)
        text_surface = my_font.render(Path(dir).stem, True, Pourpre)
        screen.blit(text_surface, (70, 100))
        clock.tick(60)
    else :
        x=0
    time += 0.0007*tempo
    # this is used to limite the runtime
    # by using for example 
    # clock.tick(50) once per frame, 
    # the script will not run faster than 50 frames per second.


pygame.quit()
