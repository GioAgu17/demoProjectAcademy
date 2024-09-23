import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Faccia con forme geometriche")

# Colori
bianco = (255, 255, 255)
nero = (0, 0, 0)
blu = (0, 0, 255)
rosso = (255, 0, 0)
# Crea un oggetto Clock per gestire il frame rate
orologio = pygame.time.Clock()

# Imposta il frame rate desiderato (ad esempio 60 FPS)
frame_rate = 60

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
    
    
    screen.fill(bianco)

    # Cerchio per la testa
    pygame.draw.circle(screen, (255, 220, 180), (400, 300), 100)

    #Cerchi per gli occhi
    pygame.draw.circle(screen, nero, (370 , 270), 10)
    pygame.draw.circle(screen, nero, (430 ,270), 10)

    # Linea per il naso
    pygame.draw.line(screen, nero, (400, 280), (400, 320), 3)

    # Rettangolo per la bocca
    pygame.draw.rect(screen, rosso, (370, 340, 60, 20), 0)
    
    orologio.tick(frame_rate)
    
    
    
    pygame.display.update()
    
    