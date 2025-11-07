import pygame
from datos.constantes import ANCHO
from .render_elementos import logo_juego, fondo_menu


def pantalla_principal(pantalla):
    logo = logo_juego()
    fondo = fondo_menu()
    
    # Obtenemos medidas del logo
    ancho_logo = logo.get_width()
    alto_logo = logo.get_height()

    # Declaramos la posición en al que queremos nuestro logo en la pantalla
    x_logo = (ANCHO - ancho_logo) // 2
    y_logo = 10

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (x_logo, y_logo))
    pygame.display.flip()
