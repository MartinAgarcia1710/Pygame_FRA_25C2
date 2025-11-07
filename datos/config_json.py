import json
import os
# Módulo destinado a manipular las configuraciones de nuestro juego enlazando archivo json
configuracion_default = {
    "config": {
        "ventana": {"ancho": 800, "alto": 600, "titulo": "Jueguito"},
        "audio": {"volumen": 0.7},
        "colores": {"fondo": [5, 1, 87], "primario": [], "secundario": [], "texto_claro": [], "texto_oscuro": []}
    }
}

archi_config = "datos/config.json"

def guardar_datos(datos):
    with open(archi_config, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def cargar_datos():
    # Si no existe o está vacío -> Creamos archivo
    if not os.path.exists(archi_config) or os.path.getsize(archi_config) == 0:
        guardar_datos(configuracion_default)
        return configuracion_default
    
    # Si existe -> Cargamos json
    with open(archi_config, "r") as archivo:
        datos = json.load(archivo)

    # Validación mínima de estructura
    if "config" not in datos:
        guardar_datos(configuracion_default)
        return configuracion_default
    
    return datos

    