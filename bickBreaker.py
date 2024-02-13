import pygame
import sys

from pygame.sprite import AbstractGroup

ANCHO = 640
ALTO = 480
color_azul = (0 , 0, 64) # Color azul para el fondo

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
        # Establecer velocidad inicial
        self.speed = [3, 3]

    def update(self):
        # Evitar que salga por debajo
        if self.rect.bottom >= ALTO or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

        # Mover en base a posición actual y velocidad
        self.rect.move_ip(self.speed)

# Inicializando pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Configurar el título de la pantalla
pygame.display.set_caption('Brick Breaker')

# Crear el reloj
reloj = pygame.time.Clock()

bolita = Bolita()

while True:
    # Establecer FPS
    reloj.tick(60)

    # Revisar todos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    # Actualizar posición de la bolita
    bolita.update()

    pantalla.fill(color_azul)

    # Dibujar bolita en pantalla
    pantalla.blit(bolita.image, bolita.rect)

    # Actualizar los elementos en pantalla
    

    pygame.display.flip()

