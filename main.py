
# Formatos de imágen que Pygame soporta:
#       - .png
#       - .jpg
#       - .webp
#       - .bmp

# Enlaces útiles
#   - Códigos de colores: https://htmlcolorcodes.com/es/
#   - Remover fondos de imágenes: https://www.remove.bg/es


# -----------------------------------------------------------------------------------
import pygame 
import datos.constantes as con
from render.render_pantalla import pantalla_principal
# Ciclo de vida de un videojuego con Pygame

#   1. Inicialización
pygame.init()
pantalla = pygame.display.set_mode((con.ANCHO, con.ALTO))
pygame.display.set_caption(con.TITULO)
reloj = pygame.time.Clock()
FPS = 60

#   2. Bucle principal
ejecutando = True

while ejecutando:
    # Finaliza el loop de juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Lógica de juego
    

    pantalla_principal(pantalla)
    # Actualización de pantalla
    pygame.display.flip()

    # Velocidad de frames por segundo
    reloj.tick(FPS)

# Finalización del programa total
pygame.quit()
