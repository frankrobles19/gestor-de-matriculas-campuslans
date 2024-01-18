from fileManager import*
# Función para registrar camper
def registrar_camper():
    print("\n-------- Registrar Camper --------")
    nro_identificacion = input("Ingrese número de identificación: ")
    nombre = input("Ingrese nombre: ")
    apellidos = input("Ingrese apellidos: ")
    direccion = input("Ingrese dirección: ")
    acudiente = input("Ingrese acudiente: ")
    celular = input("Ingrese número de celular: ")
    fijo = input("Ingrese número fijo: ")
    estado = "inscrito"

    nuevo_camper = {
        "nro_identificacion": nro_identificacion,
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefonos": {"celular": celular, "fijo": fijo},
        "estado": estado
    }

    campers_data.append(nuevo_camper)
    guardar_campers()
    print("Camper registrado con éxito.")
    main()

# Función para crear ruta de entrenamiento
def crear_ruta_entrenamiento():
    print("\n-------- Crear Ruta de Entrenamiento --------")
    nombre_ruta = input("Ingrese el nombre de la ruta: ")

    nueva_ruta = {
        "nombre": nombre_ruta,
        
    }

    rutas_entrenamiento.append(nueva_ruta)
    guardar_rutas_entrenamiento()
    print("Ruta de entrenamiento creada con éxito.")
    main()

# Función para registrar notas de prueba

def registrar_notas_prueba():
    print("\n-------- Registrar Notas de Prueba --------")
    nro_identificacion = input("Ingrese número de identificación del camper: ")
    camper = next((c for c in campers_data if c["nro_identificacion"] == nro_identificacion), None)

    if camper and camper["estado"] == "inscrito":
        nota_teoria = float(input("Ingrese la nota teórica: "))
        nota_practica = float(input("Ingrese la nota práctica: "))

        promedio = (nota_teoria + nota_practica) / 2

        if promedio >= 60:
            print("Prueba aprobada. Actualizando estado del camper.")
            camper["estado"] = "aprobado"
            guardar_campers()
            main()
        else:
            print("Prueba no aprobada.")
            main()
    else:
        print("Camper no encontrado o no inscrito.")
        main()

# Función para registrar áreas de entrenamiento
def registrar_areas_entrenamiento():
    print("\n-------- Registrar Áreas de Entrenamiento --------")
    nombre_area = input("Ingrese el nombre del área: ")
    capacidad_maxima = int(input("Ingrese la capacidad máxima del área: "))
    
    nueva_area = {
        "nombre": nombre_area,
        "capacidad_maxima": capacidad_maxima,
        "campers_asignados": []
    }

    areas_entrenamiento.append(nueva_area)
    guardar_areas_entrenamiento()
    print("Área de entrenamiento registrada con éxito.")
    main()

# Función para crear rutas de entrenamiento
def crear_ruta_entrenamiento():
    print("\n-------- Crear Ruta de Entrenamiento --------")
    nombre_ruta = input("Ingrese el nombre de la ruta: ")
    area_ruta = input("Ingrese el nombre del área de la ruta: ")  # Corregido
    nombre_entrenador = input("Ingrese el nombre del entrenador: ")

    nueva_ruta = {
        "nombre": nombre_ruta,
        "area_ruta": area_ruta,  # Corregido
        "nombre_entrenador": nombre_entrenador
    }

    rutas_entrenamiento.append(nueva_ruta)
    guardar_rutas_entrenamiento()
    print("Ruta de entrenamiento creada con éxito.")
    main()

# Función para asignar camper a ruta
def asignar_camper_a_ruta():
    print("\n-------- Asignar Camper a Ruta --------")
    nro_identificacion = input("Ingrese número de identificación del camper: ")
    camper = next((c for c in campers_data if c["nro_identificacion"] == nro_identificacion), None)

    if camper and camper["estado"] == "aprobado":
        if not rutas_entrenamiento or not areas_entrenamiento:
            print("No hay rutas o áreas disponibles. Por favor, regístrelas primero.")
            main()
            return

        print("Rutas disponibles:")
        for i, ruta in enumerate(rutas_entrenamiento, start=1):
            print(f"{i}. {ruta['nombre']}")

        opcion_ruta = int(input("Seleccione la ruta deseada (número): "))

        if 1 <= opcion_ruta <= len(rutas_entrenamiento):
            ruta_seleccionada = rutas_entrenamiento[opcion_ruta - 1]

            # Agrega la línea aquí para obtener el área de la ruta seleccionada
            area_ruta = next((a for a in areas_entrenamiento if a["nombre"] == ruta_seleccionada["area_ruta"]), None)

            if area_ruta and len(area_ruta["campers_asignados"]) < area_ruta["capacidad_maxima"]:
                area_ruta["campers_asignados"].append(camper)
                print(f"Camper asignado a la ruta {ruta_seleccionada['nombre']} con éxito.")
                guardar_areas_entrenamiento()
                main()
            else:
                print("Capacidad máxima del área alcanzada. No se puede asignar el camper.")
                main()
        else:
            print("Opción de ruta no válida.")
            main()
    else:
        print("Camper no encontrado o no aprobado.")
        main()


def asignar_entrenador_a_ruta():
    print("\n-------- Asignar Entrenador a Ruta --------")
    nombre_entrenador = input("Ingrese el nombre del entrenador: ")

    print("Rutas disponibles:")
    for i, ruta in enumerate(rutas_entrenamiento, start=1):
        print(f"{i}. {ruta['nombre']}")

    opcion_ruta = int(input("Seleccione la ruta deseada (número): "))
    
    if 1 <= opcion_ruta <= len(rutas_entrenamiento):
        ruta_seleccionada = rutas_entrenamiento[opcion_ruta - 1]

        entrenador = {
            "nombre": nombre_entrenador,
        }
        if "entrenadores_asignados" not in ruta_seleccionada:
            ruta_seleccionada["entrenadores_asignados"] = []

        ruta_seleccionada["entrenadores_asignados"].append(entrenador)
        guardar_rutas_entrenamiento()
        print(f"Entrenador asignado a la ruta {ruta_seleccionada['nombre']} con éxito.")
        main()
    else:
        print("Opción de ruta no válida.")
        main()


def gestionar_matriculas():
    print("\n-------- Gestor de Matrículas --------")
    nro_identificacion = input("Ingrese número de identificación del camper: ")
    camper = next((c for c in campers_data if c["nro_identificacion"] == nro_identificacion), None)
    print("0")

    if camper and camper["estado"] == "aprobado":
        print("Rutas disponibles:")
        for i, ruta in enumerate(rutas_entrenamiento, start=1):
            print(f"{i}. {ruta['nombre']}")

        opcion_ruta = int(input("Seleccione la ruta deseada (número): "))
        print("1")
        
        if 1 <= opcion_ruta <= len(rutas_entrenamiento):
            ruta_seleccionada = rutas_entrenamiento[opcion_ruta - 1]
            print("2")

            # Verificar capacidad del área de entrenamiento
            area_ruta = next((a for a in areas_entrenamiento if a["nombre"] == ruta_seleccionada["area_ruta"]), None)
            print (f"Area ruta: {area_ruta}")
            print(f"Campers asignados: {area_ruta['campers_asignados']}")
       

            if area_ruta:
                print(f"Capacidad máxima del área: {area_ruta['capacidad_maxima']}")
                print(f"Campers asignados en el área: {len(area_ruta['campers_asignados'])}")
                main()
                if len(area_ruta["campers_asignados"]) < area_ruta["capacidad_maxima"]:
                   print("")
                else:
                    print("Capacidad máxima del área alcanzada. No se puede matricular al camper.")
            else:
                print("Área de entrenamiento no encontrada.")
        else:
            print("Opción de ruta no válida.")
            main()
    else:
        print("Camper no encontrado o no aprobado.")
        main()



def evaluar_campers():
    print("\n-------- Evaluar Campers --------")
    nro_identificacion = input("Ingrese número de identificación del camper: ")
    camper = next((c for c in campers_data if c["nro_identificacion"] == nro_identificacion), None)

    if camper and camper["estado"] == "aprobado":
        print("Notas del camper:")
        notas = {
            "nota_teoria": float(input("Ingrese la nota teórica: ")),
            "nota_practica": float(input("Ingrese la nota práctica: "))
        }

        quices = float(input("Ingrese la nota de quices: "))

      
        promedio = (notas["nota_teoria"] * 0.3) + (notas["nota_practica"] * 0.6) + (quices * 0.1)

        if promedio >= 60:
            print("Camper aprobado en el módulo.")
            main()
        else:
            print("Camper reprobado en el módulo.")
            main()
    else:
        print("Camper no encontrado o no aprobado.")
        main()


def verificar_riesgo(camper):
    # Calculamos el promedio de las notas
    promedio_notas = sum(camper.get("notas", {}).values()) / len(camper.get("notas", {}))

    # Si el promedio es menor a 60, el camper está en riesgo
    return promedio_notas < 60

# Función para listar campers en riesgo
def campers_en_riesgo(camper):
    print("\n-------- Estudiantes en Riesgo --------")
    campers_riesgo = [camper for camper in campers_data if camper["estado"] == "aprobado" and verificar_riesgo(camper)]
    
    if campers_riesgo:
        print("Campers en riesgo:")
        for camper in campers_riesgo:
            print(f"- {camper['nombre']} {camper['apellidos']} (ID: {camper['nro_identificacion']})")
    else:
        print("No hay campers en riesgo.")


# Función para listar campers por estado
def listar_campers_por_estado(estado):
    print(f"\n-------- Listar Campers en Estado: {estado.capitalize()} --------")
    campers_estado = [camper for camper in campers_data if camper["estado"] == estado]
    
    if campers_estado:
        print(f"Campers en estado {estado}:")
        for camper in campers_estado:
            print(f"- {camper['nombre']} {camper['apellidos']} (ID: {camper['nro_identificacion']})")
    else:
        print(f"No hay campers en estado {estado}.")


def estadisticas_aprobacion_reprobacion(rutas_entrenamiento):
    print("\n-------- Estadísticas de Aprobación y Reprobación --------")
    for ruta in rutas_entrenamiento:
        print(f"\nRuta: {ruta['nombre']}")
        for entrenador in ruta.get("entrenadores_asignados", []):
            campers_ruta_entrenador = [matricula["camper"] for matricula in matriculas if matricula["ruta"] == ruta and matricula["entrenador"] == entrenador]
            
            if campers_ruta_entrenador:
                aprobados = sum(1 for camper in campers_ruta_entrenador if campers_en_riesgo(camper))
                reprobados = len(campers_ruta_entrenador) - aprobados

                print(f"\nEntrenador: {entrenador['nombre']}")
                print(f"Aprobados: {aprobados}")
                print(f"Reprobados: {reprobados}")
                main()
            else:
                print(f"\nEntrenador: {entrenador['nombre']}")
                print("No hay campers asignados.")
                main()
    print("\n")



def menu():
        
        print("""
        +++++++++++++++++++++++++++++++++++++++
        ++++ PROGRAMA REGISTRO CAMPUSLANDS ++++
       +++++++++++++++++++++++++++++++++++++++  
 """)
        print("\n\n--- MENÚ PRINCIPAL ---")
        print("1. registrar ususario")
        print("2. refistrar notas prueba")
        print("3. registrar areas de entrenamiento")
        print("4. crear ruta de entrenamiento")
        print("5. asignar campers a una ruta")
        print("6. asignar entrenador a ruta")
        print("7. gestor de matriculas")
        print("8. gestor de evaluacion")
        print("9. estudiantes en riesgo")
        print("10. modulo de reportes")

def main():
 
    menu()
    try:
        option = int(input('Seleccione una opción del menú: '))
        if option == 1:
            registrar_camper()
        elif option == 2:
            registrar_notas_prueba()
        elif option == 3:
            registrar_areas_entrenamiento()
        elif option == 4:
            crear_ruta_entrenamiento()
        elif option == 5:
            asignar_camper_a_ruta()
        elif option == 6:
            asignar_entrenador_a_ruta()
        elif option == 7:
            gestionar_matriculas()
        elif option == 8:
            evaluar_campers()
        elif option == 9:
            campers_en_riesgo()
        elif option == 10:
            listar_campers_por_estado()
        elif option == 11:
            estadisticas_aprobacion_reprobacion()
    except:
        pass


if __name__ == "__main__":
    main()




