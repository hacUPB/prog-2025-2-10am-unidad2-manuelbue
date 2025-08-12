def algoritmo_notas():
    total = 0
    for i in range(1, 7):
        nota = float(input(f"Ingrese la nota {i}: "))
        total += nota

    promedio = total / 6
    nota7 = (3.0 - (promedio * 0.7)) / 0.3

    if nota7 > 5.0:
        print("No es posible aprobar con las notas actuales")
    elif nota7 < 0:
        print("Ya aprobaste incluso si sacas 0")
    else:
        print(f"Necesitas sacar al menos: {nota7:.2f}")


def algoritmo_viaje_escolar():
    alumnos = int(input("Ingrese la cantidad de alumnos: "))
    if alumnos >= 100:
        costo_alumno = 65
    elif alumnos > 50:
        costo_alumno = 70
    elif alumnos >= 30:
        costo_alumno = 95
    else:
        costo_total = 4000
        costo_alumno = costo_total / alumnos
        print(f"Costo por alumno: ${costo_alumno:.2f}")
        print(f"Costo total: ${costo_total:.2f}")
        return

    costo_total = costo_alumno * alumnos
    print(f"Costo por alumno: ${costo_alumno:.2f}")
    print(f"Costo total: ${costo_total:.2f}")

def cantidad_de_holas():
    veces = int(input("cuantas veces quieres escribir la palabra:"))

    contador = 0
    while contador <veces:
        print("hola puto")
        contador = contador + 1

def calcular_edad():
    dia_act = int(input("Día actual: "))
    mes_act = int(input("Mes actual: "))
    año_act = int(input("Año actual: "))

    dia_nac = int(input("Día de nacimiento: "))
    mes_nac = int(input("Mes de nacimiento: "))
    año_nac = int(input("Año de nacimiento: "))

    # Calcular diferencia de años
    edad = año_act - año_nac

    # Ajustar si aún no ha cumplido años este año
    if mes_act < mes_nac or (mes_act == mes_nac and dia_act < dia_nac):
        edad -= 1

    print("La edad es:", edad, "años")

# ==============================
# SELECCIÓN DE ALGORITMO
# ==============================
print("Selecciona el algoritmo a ejecutar:")
print("1. Calcular nota necesaria para aprobar")
print("2. Costo por alumno en viaje escolar")
print("3. Cantidad de holas")
print("4. calcular edad")
opcion = input("Ingresa 1, 2, 3 o 4: ")

if opcion == "1":
    algoritmo_notas()
elif opcion == "2":
    algoritmo_viaje_escolar()
elif opcion == "3":
    cantidad_de_holas()
elif opcion == "4":
    calcular_edad()
else:
    print("Opción no válida")
