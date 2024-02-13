import pygame
import sys

from pygame.sprite import AbstractGroup

ANCHO = 640
ALTO = 480

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('imagenes/bolita.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla
        self.rect.centerx = ANCHO/2
        self.rect.centery = ALTO/2

# Inicializand pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Configurar el título de la pantalla
pygame.display.set_caption('Brick Breaker')

bolita = Bolita()

while True:
    # Revisar todos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    # Dibujar bolita en pantalla
    pantalla.blit(bolita.image, bolita.rect)

    # Actualizar los elementos en pantalla
    

    pygame.display.flip()

