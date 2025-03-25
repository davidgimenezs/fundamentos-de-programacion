# Diccionario de meses en español
MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

def validar_entero_positivo(valor):
    """Verifica que un valor es un entero positivo."""
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            raise ValueError
    except ValueError:
        print("Error: Debes ingresar un número entero positivo.")
        exit()

def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    """Devuelve la cantidad de días en un mes dado."""
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif mes in {4, 6, 9, 11}:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    else:
        return 0

def validar_fecha(dia, mes, anio):
    """Verifica que la fecha ingresada es válida."""
    if mes < 1 or mes > 12 or dia < 1 or dia > dias_en_mes(mes, anio) or anio < 1:
        print(f"Error: La fecha {dia},{mes},{anio} no es válida.")
        exit()
    return dia, mes, anio

def calcular_fecha_futura(dia, mes, anio):
    """Calcula la fecha 15 días después manualmente."""
    dia += 15
    while dia > dias_en_mes(mes, anio):
        dia -= dias_en_mes(mes, anio)
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return dia, mes, anio

# Solicitar cantidad de fechas
n = input("Ingresa la cantidad de fechas a procesar: ")
n = validar_entero_positivo(n)

# Almacenar fechas y resultados
fechas_procesadas = []

# Recibir todas las fechas primero
for _ in range(n):
    entrada = input("Ingresa una fecha en formato día,mes,año: ")
    try:
        dia, mes, anio = map(int, entrada.split(","))
    except ValueError:
        print("Error: Formato de fecha incorrecto. Usa día,mes,año con números enteros.")
        exit()
    
    # Validar la fecha
    dia, mes, anio = validar_fecha(dia, mes, anio)
    
    # Calcular la nueva fecha
    dia_nuevo, mes_nuevo, anio_nuevo = calcular_fecha_futura(dia, mes, anio)
    
    # Almacenar resultado
    fechas_procesadas.append((dia_nuevo, mes_nuevo, anio_nuevo))

# Imprimir todas las fechas después de recibir todas las entradas
for dia, mes, anio in fechas_procesadas:
    print(f"{dia}, {MESES[mes]} de {anio}")
