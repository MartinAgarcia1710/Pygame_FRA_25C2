import datos.config_json as config_json

datos = config_json.cargar_datos()
ANCHO = datos["config"]["ventana"]["ancho"] # Me va a dar el valor de la clave "ancho" en nuestro archivo json
ALTO = datos["config"]["ventana"]["alto"] # Me va a dar el valor de la clave "alto" en nuestro archivo json
COLOR_FONDO = datos["config"]["colores"]["fondo"] # Me va a dar el valor de la clave "fondo" en nuestro archivo json
TITULO = datos["config"]["ventana"]["titulo"] # Me va a dar el valor de la clave "titulo" en nuestro archivo json
COLOR_TEXTO_OSCURO = datos["config"]["colores"]["texto_oscuro"]
COLOR_TEXTO_CLARO = datos["config"]["colores"]["texto_claro"]
COLOR_SECUNDARIO =  datos["config"]["colores"]["primario"]
VOLUMEN = datos["config"]["audio"]["volumen"]
# Siempre que querramos entrar en la configuración de nuestro json lo hacemos a travéz del módulo constantes.py

# main.py -> constantes.py -> config_json.py