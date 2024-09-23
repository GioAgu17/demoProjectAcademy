import pygame
import sys

# inizializza tutti i moduli di Pygame
pygame.init()

# Definisci le dimensioni della finestra
dimensioni = (1280, 720)

# Crea una finestra di gioco
finestra = pygame.display.set_mode(dimensioni)

# Imposta il titolo della finestra
pygame.display.set_caption("Test di installazione Pygame")

# Imposta icona della finestra
icona = pygame.image.load("bulbasaur.jpg")
pygame.display.set_icon(icona)

# Definisci un colore di sfondo (RGB)
sfondo_colore = (150, 200, 250)

# Crea un oggetto Clock per gestire il frame rate
orologio = pygame.time.Clock()

# Imposta il frame rate desiderato (ad esempio 60 FPS)
frame_rate = 60

# Aggiunta di un commento inutile per un commit di test

# Loop principale del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # pygame.KEYDOWN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    
    # Riempi la finestra con il colore di sfondo
    finestra.fill(sfondo_colore)


    # Aggiorna il display
    pygame.display.update()

    # Limita il frame rate al valore specificato
    orologio.tick(frame_rate)