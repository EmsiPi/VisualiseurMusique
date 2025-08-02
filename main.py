import pygame
import math
import numpy as np
import librosa
from pathlib import Path

import librosa
import matplotlib.pyplot as plt

# Chargement du fichier audio
y, sr = librosa.load('SquareASaw-Lover.mp3')

# Création du vecteur temps (x-axis)
temps = librosa.times_like(y, sr=sr)

# Affichage de la forme d’onde
plt.figure(figsize=(12, 4))
plt.plot(temps, y, color='purple')
plt.title('Forme d’onde de SquareASaw-Lover')
plt.xlabel('Temps (secondes)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()
# --- Initialisation ---
pygame.init()
pygame.font.init()
pygame.mixer.init()

# --- Constantes de couleur ---
Pourpre = (50, 0, 20)
Violet = (160, 32, 240)
Jaune = (255, 100, 20)
Magenta = (0, 255, 255)
Vert = (0, 255, 0)
Couleurs = [Pourpre, Violet, Jaune, Magenta, Vert]

# --- Dimensions de la fenêtre ---
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GroovingEnPleineLiberté')
clock = pygame.time.Clock()

# --- Chargement de la musique ---
music_path = 'SquareASaw-Lover.mp3'
y, sr = librosa.load(music_path)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
tempo = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)
tempo_val = tempo[0][0] if tempo.shape[1] > 0 else 120  # bpm par défaut

# --- Interface graphique ---
background_colour = (200, 200, 250)
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render(Path(music_path).stem, True, Pourpre)

# --- Chargement et lecture audio ---
sound = pygame.mixer.Sound(music_path)
sound.set_volume(0.2)
sound.play()

# --- Classe pour un bouton (utilisable plus tard pour changer de musique) ---
class Button:
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = pygame.transform.scale(image, (150, 60))
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.text_input = text_input
        self.text = my_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(x_pos, y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_click(self, pos):
        return self.rect.collidepoint(pos)

# --- Bouton (pas encore fonctionnel, à implémenter) ---
# button_img = pygame.image.load('arrow.png').convert_alpha()
# button = Button(button_img, WIDTH - 100, HEIGHT - 50, "Changer")

# --- Animation principale ---
time = 0
running = True

while running:
    screen.fill(background_colour)
    screen.blit(text_surface, (70, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # À compléter plus tard : interaction avec bouton
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if button.check_click(event.pos):
        #         print("Changer de musique !")

    # --- Couleurs variables pour animation ---
    r = int((math.sin(time) + 1) * 127.5)
    g = int((math.sin(time + 2) + 1) * 127.5)
    b = int((math.sin(time + 4) + 1) * 127.5)
    radius = int((math.sin(time) + 1) * 50 + 10)
    
    pygame.draw.circle(screen, (r, g, b), CENTER, radius)

    # --- Affichage bouton (non fonctionnel pour l'instant) ---
    # button.update()

    pygame.display.flip()
    clock.tick(60)
    time += 0.0007 * tempo_val  # Ajustement selon tempo

pygame.quit()

# --- TODO ---
# 1. Ajouter une liste de musiques et permettre de changer avec le bouton
# 2. Afficher une animation différente selon la musique (par exemple : vitesse/couleurs)
# 3. Ajouter un affichage de texte réactif (battements ?)
# 4. Nettoyer les ressources / charger dynamiquement
# 5. Ajouter une barre de progression musicale ?
