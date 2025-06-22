import pygame
   
(width, height) = (400, 300)
screen = pygame.display.set_mode((width, height))

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
from pathlib import Path
background_colour = (255,200,200)
screen.fill(background_colour)
dir = 'SquareASaw-Lover.mp3'
text_surface = my_font.render(Path(dir).stem, True, (0, 0, 0))
screen.blit(text_surface, (70,100))

pygame.display.set_caption('GroovingEnPleineLiberté') #Nom de la fenêtre 



pygame.mixer.init() #mixer de musique
pygame.mixer.music.load('SquareASaw-Lover.mp3') #load le fichier mp3
pygame.mixer.music.play() #play le fichier mp3

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False