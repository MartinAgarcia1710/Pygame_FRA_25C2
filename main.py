# En caso de que quede remarcado en amarillo ejecutar el siguietne comando:
#                               python -m pip install pygame --upgrade

# Pygame es una biblioteca gráfica que nos permite realizar apps tipo juegos de manera sencilla
# Otra biblioteca para interfaz gráfica (No juegos) es tkinter

# Formatos de imágen que Pygame soporta:
#       - .png
#       - .jpg
#       - .webp
#       - .bmp

# Enlaces útiles
#   - Códigos de colores: https://htmlcolorcodes.com/es/
#   - Remover fondos de imágenes: https://www.remove.bg/es
#   - Assets
#       - https://itch.io/
#       - https://kenney.nl/


# -----------------------------------------------------------------------------------
import pygame 
import datos.constantes as con
from render.render_pantalla import pantalla_principal, pantalla_opciones
from gestor_eventos.eventos import gestionar_eventos
from audio.gestor_audio import reproducir_musica, MUSICA_PRINCIPAL
# Ciclo de vida de un videojuego con Pygame

#   1. Inicialización
pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((con.ANCHO, con.ALTO))
pygame.display.set_caption(con.TITULO)
reloj = pygame.time.Clock()
FPS = 60
pantalla_actual = "menu"
musica_actual = None

botones = None
#   2. Bucle principal
ejecutando = True

while ejecutando:
    # Finaliza el loop de juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        else:
            pantalla_actual = gestionar_eventos(evento, pantalla_actual, botones)
        
    # Lógica de juego
    if pantalla_actual == "menu":
        if musica_actual != "menu":
            reproducir_musica(MUSICA_PRINCIPAL)
            musica_actual = "menu"
        botones = pantalla_principal(pantalla)

    elif pantalla_actual == "jugar":
        botones = None
    elif pantalla_actual == "opciones":
        botones = pantalla_opciones(pantalla)
    elif pantalla_actual == "creditos":
        botones = None
    elif pantalla_actual == "estadisticas":
        botones = None
    elif pantalla_actual == "salir":
        pass
    
    # Actualización de pantalla
    pygame.display.flip()

    # Velocidad de frames por segundo
    reloj.tick(FPS)

# Finalización del programa total
pygame.quit()