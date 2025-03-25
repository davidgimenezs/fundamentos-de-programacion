def monitorear_temperatura():
    temperaturas_validas = []
    mediciones_invalidas = 0
    
    while True:
        try:
            temperatura = float(input().strip())
        except ValueError:
            print("Entrada no válida. Ingrese un número.")
            continue
        
        if not (0 <= temperatura <= 1000):
            print("¡Alarma! Temperatura fuera del rango permitido (0°C - 1000°C).")
            mediciones_invalidas += 1
            if mediciones_invalidas >= 3:
                print("Se han ingresado más de 3 mediciones inválidas. Finalizando el programa.")
                return
            continue
        
        print(f"Temperatura actual {temperatura}")
        temperaturas_validas.append(temperatura)
        mediciones_invalidas = 0
        
        if len(temperaturas_validas) == 3:
            promedio = sum(temperaturas_validas) / 3
            print(f"Promedio {promedio}")
            if abs(temperatura - promedio) > 20:
                print("¡Alarma! Se ha detectado una fluctuación inesperada en la temperatura.")
            else:
                print("La temperatura está dentro del rango normal.")
            temperaturas_validas.clear()

monitorear_temperatura()