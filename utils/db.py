import os
import json

RUTA_TAREAS = "tareas.json"

def cargar_tareas():
    if not os.path.exists(RUTA_TAREAS):
        return []
    with open(RUTA_TAREAS, "r") as archivo:
        return json.load(archivo)

def guardar_tareas(tareas):
    with open(RUTA_TAREAS, "w") as archivo:
        json.dump(tareas, archivo, indent=2)

def añadir_tarea(tarea):
    tareas = cargar_tareas()
    tareas.append(tarea)
    guardar_tareas(tareas)

def listar_tareas():
    return cargar_tareas()

def eliminar_tarea(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        guardar_tareas(tareas)
        return True
    return False