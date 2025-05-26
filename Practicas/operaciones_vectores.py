import random

def validar_entrada():
    """
    Valida que la entrada sea un número entero positivo.
    Retorna el número validado.
    """
    while True:
        try:
            n = int(input("Ingrese un número entero y positivo N: "))
            if n > 0:
                return n
            else:
                print("Error: Debe ingresar un número positivo mayor que 0.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def generar_vector(n):
    """
    Genera un vector de N componentes con números aleatorios entre -50 y 50.
    Parámetros:
        n (int): Número de componentes del vector
    Retorna:
        list: Vector generado con números aleatorios
    """
    vector = []
    for i in range(n):
        numero = random.randint(-50, 50)
        vector.append(numero)
    return vector

def obtener_subsecuencias(vector):
    """
    Encuentra todas las subsecuencias contiguas del vector y calcula sus sumas.
    Parámetros:
        vector (list): Vector de entrada
    Retorna:
        list: Lista de tuplas con (subsecuencia, suma, índice_inicio, índice_fin)
    """
    subsecuencias = []
    n = len(vector)
    
    for i in range(n):
        for j in range(i, n):
            # Extraer subsecuencia desde índice i hasta j (inclusive)
            subsecuencia = vector[i:j+1]
            suma = sum(subsecuencia)
            subsecuencias.append((subsecuencia, suma, i, j))
    
    return subsecuencias

def encontrar_mayor_suma(subsecuencias):
    """
    Encuentra la subsecuencia con la mayor suma.
    En caso de empate, retorna la primera encontrada.
    Parámetros:
        subsecuencias (list): Lista de subsecuencias con sus datos
    Retorna:
        tuple: Datos de la subsecuencia con mayor suma
    """
    if not subsecuencias:
        return None
    
    mayor_suma = subsecuencias[0][1]  # Suma de la primera subsecuencia
    mejor_subsecuencia = subsecuencias[0]
    
    for subsec_data in subsecuencias:
        if subsec_data[1] > mayor_suma:
            mayor_suma = subsec_data[1]
            mejor_subsecuencia = subsec_data
    
    return mejor_subsecuencia

def imprimir_vector(vector):
    """
    Imprime el vector de manera clara y ordenada.
    Parámetros:
        vector (list): Vector a imprimir
    """
    print(f"Vector generado: {vector}")
    print(f"Longitud del vector: {len(vector)}")

def imprimir_todas_subsecuencias(subsecuencias):
    """
    Imprime todas las subsecuencias encontradas con formato claro.
    Parámetros:
        subsecuencias (list): Lista de todas las subsecuencias
    """
    print("\n" + "="*60)
    print("TODAS LAS SUBSECUENCIAS ENCONTRADAS:")
    print("="*60)
    
    for i, (subsec, suma, ini, fin) in enumerate(subsecuencias, 1):
        print(f"{i:2d}. Subsecuencia: {subsec}")
        print(f"    Suma: {suma}")
        print(f"    Índices: desde {ini} hasta {fin}")
        print("-" * 40)

def imprimir_resultado_principal(mejor_subsecuencia):
    """
    Imprime el resultado principal con la subsecuencia de mayor suma.
    Parámetros:
        mejor_subsecuencia (tuple): Datos de la mejor subsecuencia
    """
    subsec, suma, ini, fin = mejor_subsecuencia
    
    print("\n" + "="*60)
    print("RESULTADO PRINCIPAL:")
    print("="*60)
    print(f"La mayor suma que puede obtenerse con una subsecuencia de elementos contiguos es: {suma}")
    print(f"Subsecuencia: {subsec}")
    print(f"Índices de la subsecuencia: desde {ini} hasta {fin}")
    print("="*60)
"""
Función principal que coordina la ejecución del programa.
"""
print("="*60)
print("PROGRAMA DE ANÁLISIS DE VECTORES Y SUBSECUENCIAS")
print("="*60)

# 1. Validar entrada
n = validar_entrada()

# 2. Generar vector aleatorio
vector = generar_vector(n)

# 3. Imprimir vector generado
print("\n" + "-"*40)
print("VECTOR GENERADO:")
print("-"*40)
imprimir_vector(vector)

# 4. Obtener todas las subsecuencias
subsecuencias = obtener_subsecuencias(vector)

# 5. Encontrar la subsecuencia con mayor suma
mejor_subsecuencia = encontrar_mayor_suma(subsecuencias)

# 6. Imprimir todas las subsecuencias (opcional para verificación)
respuesta = input("\n¿Desea ver todas las subsecuencias encontradas? (s/n): ").lower()
if respuesta == 's' or respuesta == 'si':
    imprimir_todas_subsecuencias(subsecuencias)

# 7. Imprimir resultado principal
imprimir_resultado_principal(mejor_subsecuencia)

print(f"\nTotal de subsecuencias analizadas: {len(subsecuencias)}")
