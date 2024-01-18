import json
# Variables para almacenar datos
campers_data = []
rutas_entrenamiento = []
areas_entrenamiento = []
entrenadores = []
matriculas = []

# Función para guardar datos en archivos JSON
def guardar_campers():
    with open("campers_data.json", "w") as file:
        json.dump(campers_data, file, indent=4)

def guardar_rutas_entrenamiento():
    with open("rutas_entrenamiento.json", "w") as file:
        json.dump(rutas_entrenamiento, file, indent=4)

def guardar_areas_entrenamiento():
    with open("areas_entrenamiento.json", "w") as file:
        json.dump(areas_entrenamiento, file, indent=4)

def guardar_entrenadores():
    with open("entrenadores.json", "w") as file:
        json.dump(entrenadores, file, indent=4)

def guardar_matriculas():
    with open("matriculas.json", "w") as file:
        json.dump(matriculas, file, indent=4)

# Función para cargar datos desde archivos JSON
def cargar_datos():
    global campers_data, rutas_entrenamiento, areas_entrenamiento, entrenadores, matriculas

    try:
        with open("campers_data.json", "r") as file:
            campers_data = json.load(file)
    except FileNotFoundError:
        pass
    
    try:
        with open("rutas_entrenamiento.json", "r") as file:
            rutas_entrenamiento = json.load(file)
    except FileNotFoundError:
        pass
    
    try:
        with open("areas_entrenamiento.json", "r") as file:
            areas_entrenamiento = json.load(file)
    except FileNotFoundError:
        pass
    
    try:
        with open("entrenadores.json", "r") as file:
            entrenadores = json.load(file)
    except FileNotFoundError:
        pass
    
    try:
        with open("matriculas.json", "r") as file:
            matriculas = json.load(file)
    except FileNotFoundError:
        pass

