import math
import random

import pygame
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crear una ventana
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# Sonido
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.5)  # Ajustar el volumen de la música
mixer.music.play(-1)  # Reproduce la música en bucle

# Variables jugador
jugador_imagen = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables enemigo
enemigo_imagen = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for i in range(cantidad_enemigos):
    enemigo_imagen.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 735))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Variables bala
balas = []
bala_imagen = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

# Variables puntuacion
puntuacion = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10


# Función para mostrar la puntuación
def mostrar_puntuacion(x, y):
    puntuacion_texto = fuente.render("Puntuacion : " + str(puntuacion), True, (255, 255, 255))
    pantalla.blit(puntuacion_texto, (x, y))


# Función jugador
def jugador(x, y):
    pantalla.blit(jugador_imagen, (x, y))


# Función enemigo
def enemigo(x, y, ene):
    pantalla.blit(enemigo_imagen[ene], (x, y))


# Función disparar
def disparar(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala_imagen, (x + 16, y + 10))


# Función colisión
def hay_colision(x_1, y_1, x_2, y_2):
    # Distancia entre dos objetos
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False


# Bucle principal
se_ejecuta = True
while se_ejecuta:
    # Color de fondo
    pantalla.blit(fondo, (0, 0))
    for evento in pygame.event.get():
        # Evento de cierre
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                # Sonido de disparo
                sonido_disparo = mixer.Sound("disparo.mp3")
                sonido_disparo.set_volume(0.5)
                sonido_disparo.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

                if not bala_visible:
                    bala_x = jugador_x
                    # Disparar la bala
                disparar(bala_x, bala_y)

        # Evento  soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Movimiento del jugador
    jugador_x += jugador_x_cambio

    # Limitar el movimiento del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Movimiento del enemigo
    for i in range(cantidad_enemigos):
        # Game Over
        if enemigo_y[i] > 440:
            for j in range(cantidad_enemigos):
                enemigo_y[j] = 2000
            # Mostrar Game Over
            game_over_fuente = pygame.font.Font("freesansbold.ttf", 64)
            game_over_texto = game_over_fuente.render("GAME OVER", True, (255, 0, 0))
            pantalla.blit(game_over_texto, (200, 250))
            pygame.display.update()
            break
        # Movimiento del enemigo
        enemigo_x[i] += enemigo_x_cambio[i]
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = 0.3
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -0.3
            enemigo_y[i] += enemigo_y_cambio[i]

        # Colisión
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[i], enemigo_y[i], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntuacion += 1
                enemigo_x[i] = random.randint(0, 736)
                enemigo_y[i] = random.randint(20, 200)
                break

        enemigo(enemigo_x[i], enemigo_y[i], i)

    # Movimiento de la bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(bala_imagen, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    jugador(jugador_x, jugador_y)
    mostrar_puntuacion(texto_x, texto_y)

    # Actualizar la pantalla
    pygame.display.update()
