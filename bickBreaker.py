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

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('imagenes/paleta.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla en X
        self.rect.midbottom = (ANCHO/2, ALTO - 20)
        # Establecer velocidad inicial
        self.speed = [0, 0]

    def update(self, evento):
        # Buscar si se presionó la flecha izquierda
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        # Si se presionó flecha derecha
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        # Mover en base a posición actual y velocidad
        self.rect.move_ip(self.speed)

# Inicializando pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Configurar el título de la pantalla
pygame.display.set_caption('Brick Breaker')

# Crear el reloj
reloj = pygame.time.Clock()

# Ajustar repetición de evento de tecla presionada.
pygame.key.set_repeat(20)

bolita = Bolita()
jugador = Paleta()

while True:
    # Establecer FPS
    reloj.tick(60)

    # Revisar todos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        # Buscar eventos del teclado
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)

    # Actualizar posición de la bolita
    bolita.update()

    pantalla.fill(color_azul)

    # Dibujar bolita en pantalla
    pantalla.blit(bolita.image, bolita.rect)

    # Dibujar jugador en pantalla
    pantalla.blit(jugador.image, jugador.rect)
    
    # Actualizar los elementos en pantalla
    pygame.display.flip()

