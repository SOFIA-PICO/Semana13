#Código de la semana 12
# Definir la estructura de datos para almacenar temperaturas
# Ciudades: Quito, Loja, Cuenca -> Semanas -> Días de la semana
temperaturas = [
    [  # Quito
        [("Lunes", 20), ("Martes", 22), ("Miércoles", 21), ("Jueves", 19), ("Viernes", 23), ("Sábado", 24), ("Domingo", 21)],  # Semana 1
        [("Lunes", 18), ("Martes", 20), ("Miércoles", 19), ("Jueves", 21), ("Viernes", 22), ("Sábado", 23), ("Domingo", 22)],  # Semana 2
        [("Lunes", 23), ("Martes", 24), ("Miércoles", 25), ("Jueves", 22), ("Viernes", 20), ("Sábado", 21), ("Domingo", 19)],  # Semana 3
        [("Lunes", 19), ("Martes", 18), ("Miércoles", 20), ("Jueves", 21), ("Viernes", 23), ("Sábado", 22), ("Domingo", 21)]   # Semana 4
    ],
    [  # Loja
        [("Lunes", 25), ("Martes", 27), ("Miércoles", 28), ("Jueves", 26), ("Viernes", 29), ("Sábado", 30), ("Domingo", 28)],  # Semana 1
        [("Lunes", 28), ("Martes", 29), ("Miércoles", 27), ("Jueves", 26), ("Viernes", 25), ("Sábado", 28), ("Domingo", 27)],  # Semana 2
        [("Lunes", 26), ("Martes", 24), ("Miércoles", 25), ("Jueves", 23), ("Viernes", 22), ("Sábado", 24), ("Domingo", 25)],  # Semana 3
        [("Lunes", 22), ("Martes", 23), ("Miércoles", 21), ("Jueves", 20), ("Viernes", 22), ("Sábado", 23), ("Domingo", 21)]   # Semana 4
    ],
    [  # Cuenca
        [("Lunes", 18), ("Martes", 20), ("Miércoles", 22), ("Jueves", 21), ("Viernes", 19), ("Sábado", 20), ("Domingo", 21)],  # Semana 1
        [("Lunes", 22), ("Martes", 23), ("Miércoles", 24), ("Jueves", 22), ("Viernes", 23), ("Sábado", 21), ("Domingo", 20)],  # Semana 2
        [("Lunes", 20), ("Martes", 19), ("Miércoles", 21), ("Jueves", 20), ("Viernes", 18), ("Sábado", 19), ("Domingo", 17)],  # Semana 3
        [("Lunes", 19), ("Martes", 20), ("Miércoles", 22), ("Jueves", 21), ("Viernes", 23), ("Sábado", 22), ("Domingo", 24)]   # Semana 4
    ]
]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
ciudades = ["Quito", "Loja", "Cuenca"]

for i in range(len(temperaturas)):
    print(f"Promedio de temperaturas en {ciudades[i]}:")
    for j in range(len(temperaturas[i])):
        suma = 0
        print(f"  Semana {j + 1}:")
        for dia in temperaturas[i][j]:
            suma += dia[1]
            print(f"    {dia[0]}: {dia[1]}°C")
        promedio = suma / len(temperaturas[i][j])
        print(f"    -> Promedio semanal: {promedio:.2f}°C\n")
    print("-" * 40)



#A partir de aquí es la tarea de la semana 13
# Función para calcular el promedio de temperaturas por ciudad y semana
def promedio_temperatura_ciudad(temperaturas, ciudad, semana):
    # Definir las ciudades según el índice de la matriz
    ciudades = ["Quito", "Loja", "Cuenca"]

    # Buscar el índice de la ciudad
    if ciudad not in ciudades:
        return "Ciudad no encontrada"

    # Obtener el índice de la ciudad en la lista de ciudades
    indice_ciudad = ciudades.index(ciudad)

    # Validar el número de semana
    if semana < 1 or semana > len(temperaturas[indice_ciudad]):
        return "Semana no válida"

    # Extraer la semana correspondiente (semana - 1 porque los índices comienzan en 0)
    semana_temperaturas = temperaturas[indice_ciudad][semana - 1]

    # Calcular el promedio de la semana
    suma_temperaturas = sum(dia[1] for dia in semana_temperaturas)
    promedio = suma_temperaturas / len(semana_temperaturas)

    return f"El promedio de temperatura en {ciudad} durante la semana {semana} es {promedio:.2f}°C"


#Validaciones de ciudad:
print("Validaciones de ciudad:")
print(promedio_temperatura_ciudad(temperaturas, "Nueva Loja", 4))
#Validaciones de semanas
print("--------------")
print("Validaciones de semanas:")
print(promedio_temperatura_ciudad(temperaturas, "Quito", 5))
print("--------------")
print("Ejecución correcta:")
print("Datos para comparar, Ciudad Cuenca, Semana 3")
print(promedio_temperatura_ciudad(temperaturas, "Cuenca", 3))
ciudad_c = input("Ingrese el nombre de la ciudad (Quito, Loja, Cuenca): ")
semana_c = int(input("Ingrese el número de la semana (1-4): "))

# Mostrar el promedio de temperatura basado en la entrada del usuario
print(promedio_temperatura_ciudad(temperaturas, ciudad_c, semana_c))
#Comparación


