import pygame
from datos.constantes import ANCHO, ALTO

# Cargar assets UNA SOLA VEZ
LOGO = pygame.image.load("assets/logo.png")
LOGO = pygame.transform.scale(LOGO, (ANCHO / 2, ALTO / 2))

FONDO = pygame.image.load("assets/fondo_universo.jpg")
FONDO = pygame.transform.scale(FONDO, (ANCHO, ALTO))

def logo_juego():
    return LOGO

def fondo_menu():
    return FONDO
