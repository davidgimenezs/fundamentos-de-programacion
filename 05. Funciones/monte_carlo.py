import random
random.seed(42)

opcion = input()

if opcion == "1":
    # Imprimir 10 numeros entre 0 y 1
    for i in range(10):
        print(f"{random.random():.4f}")

if opcion == "2":
    rango = int(input())
    # Generar 10 puntos y contar cuantos están en el circulo
    if rango == 10:
        contador = 0
        for i in range(rango):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                contador+=1
        print(f"Se generaron {contador} números dentro del círculo")

    # Generar 10 puntos y contar cuantos están en el circulo
    if rango == 50:
        contador = 0
        for i in range(rango):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                contador+=1
        print(f"Se generaron {contador} números dentro del círculo")

if opcion == "3":
    rango = int(input())
    # Estimar pi con 10 puntos
    if rango == 10:
        contador = 0
        for i in range(rango):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                contador+=1
        estimacion = 4 * contador / rango
        print(f"El valor estimado de pi es {estimacion:.4f}")
    
    # Estimar pi con 50 puntos
    if rango == 50:
        contador = 0
        for i in range(rango):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                contador+=1
        estimacion = 4 * contador / rango
        print(f"El valor estimado de pi es {estimacion:.4f}")
        
    # Estimar pi con 500 puntos
    if rango == 500:
        contador = 0
        for i in range(rango):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                contador+=1
        estimacion = 4 * contador / rango
        print(f"El valor estimado de pi es {estimacion:.4f}")