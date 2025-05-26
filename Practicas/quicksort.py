# QuickSort - Algoritmo de ordenamiento por división y conquista
# Autor: David
# Fecha: Mayo 2025

def quicksort(arr, inicio=0, fin=None):
    """
    Algoritmo QuickSort para ordenar una lista de elementos.
    
    Parámetros:
    - arr: Lista a ordenar
    - inicio: Índice de inicio (por defecto 0)
    - fin: Índice final (por defecto len(arr)-1)
    
    Complejidad temporal:
    - Mejor caso: O(n log n)
    - Caso promedio: O(n log n)
    - Peor caso: O(n²)
    """
    if fin is None:
        fin = len(arr) - 1
    
    # Caso base: si el subarreglo tiene 1 o menos elementos
    if inicio < fin:
        # Particionar y obtener el índice del pivote
        indice_pivote = particionar(arr, inicio, fin)
        
        # Ordenar recursivamente los elementos antes y después del pivote
        quicksort(arr, inicio, indice_pivote - 1)
        quicksort(arr, indice_pivote + 1, fin)


def particionar(arr, inicio, fin):
    """
    Función de partición que coloca el pivote en su posición correcta
    y organiza los elementos menores a la izquierda y mayores a la derecha.
    
    Parámetros:
    - arr: Lista a particionar
    - inicio: Índice de inicio del subarreglo
    - fin: Índice final del subarreglo
    
    Retorna:
    - Índice donde quedó ubicado el pivote
    """
    # Elegimos el último elemento como pivote
    pivote = arr[fin]
    
    # Índice del elemento más pequeño
    i = inicio - 1
    
    for j in range(inicio, fin):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiar elementos
    
    # Colocar el pivote en su posición correcta
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1


def quicksort_con_pivote_medio(arr, inicio=0, fin=None):
    """
    Variante de QuickSort que usa el elemento del medio como pivote.
    Puede mejorar el rendimiento en listas parcialmente ordenadas.
    """
    if fin is None:
        fin = len(arr) - 1
    
    if inicio < fin:
        # Mover el elemento del medio al final para usar como pivote
        medio = (inicio + fin) // 2
        arr[medio], arr[fin] = arr[fin], arr[medio]
        
        # Usar la misma función de partición
        indice_pivote = particionar(arr, inicio, fin)
        
        quicksort_con_pivote_medio(arr, inicio, indice_pivote - 1)
        quicksort_con_pivote_medio(arr, indice_pivote + 1, fin)


def quicksort_iterativo(arr):
    """
    Implementación iterativa de QuickSort usando una pila.
    Evita el problema de desbordamiento de pila en listas muy grandes.
    """
    if len(arr) <= 1:
        return
    
    # Crear una pila para almacenar los índices
    pila = [(0, len(arr) - 1)]
    
    while pila:
        inicio, fin = pila.pop()
        
        if inicio < fin:
            # Particionar y obtener el índice del pivote
            indice_pivote = particionar(arr, inicio, fin)
            
            # Agregar los subarreglos a la pila
            pila.append((inicio, indice_pivote - 1))
            pila.append((indice_pivote + 1, fin))


def imprimir_lista(arr, descripcion=""):
    """Función auxiliar para imprimir listas de forma organizada."""
    print(f"{descripcion}: {arr}")


def pruebas_quicksort():
    """Función que ejecuta varias pruebas del algoritmo QuickSort."""
    print("=" * 60)
    print("PRUEBAS DEL ALGORITMO QUICKSORT")
    print("=" * 60)
    
    # Prueba 1: Lista desordenada
    print("\n1. Lista desordenada:")
    lista1 = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
    imprimir_lista(lista1, "Original")
    quicksort(lista1)
    imprimir_lista(lista1, "Ordenada")
    
    # Prueba 2: Lista ya ordenada
    print("\n2. Lista ya ordenada:")
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    imprimir_lista(lista2, "Original")
    quicksort(lista2)
    imprimir_lista(lista2, "Ordenada")
    
    # Prueba 3: Lista ordenada inversamente
    print("\n3. Lista ordenada inversamente:")
    lista3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    imprimir_lista(lista3, "Original")
    quicksort(lista3)
    imprimir_lista(lista3, "Ordenada")
    
    # Prueba 4: Lista con elementos repetidos
    print("\n4. Lista con elementos repetidos:")
    lista4 = [5, 2, 8, 2, 9, 1, 5, 5, 8, 3]
    imprimir_lista(lista4, "Original")
    quicksort(lista4)
    imprimir_lista(lista4, "Ordenada")
    
    # Prueba 5: Lista con un solo elemento
    print("\n5. Lista con un solo elemento:")
    lista5 = [42]
    imprimir_lista(lista5, "Original")
    quicksort(lista5)
    imprimir_lista(lista5, "Ordenada")
    
    # Prueba 6: Lista vacía
    print("\n6. Lista vacía:")
    lista6 = []
    imprimir_lista(lista6, "Original")
    quicksort(lista6)
    imprimir_lista(lista6, "Ordenada")
    
    # Prueba 7: Comparación con pivote medio
    print("\n7. Comparación con pivote del medio:")
    lista7 = [3, 6, 8, 10, 1, 2, 1]
    lista7_copia = lista7.copy()
    imprimir_lista(lista7, "Original")
    quicksort(lista7)
    imprimir_lista(lista7, "QuickSort normal")
    quicksort_con_pivote_medio(lista7_copia)
    imprimir_lista(lista7_copia, "QuickSort pivote medio")
    
    # Prueba 8: Versión iterativa
    print("\n8. Versión iterativa:")
    lista8 = [29, 10, 14, 37, 13, 28, 4, 9]
    lista8_copia = lista8.copy()
    imprimir_lista(lista8, "Original")
    quicksort(lista8)
    imprimir_lista(lista8, "QuickSort recursivo")
    quicksort_iterativo(lista8_copia)
    imprimir_lista(lista8_copia, "QuickSort iterativo")


if __name__ == "__main__":
    # Ejecutar las pruebas cuando se ejecute el archivo directamente
    pruebas_quicksort()
    
    print("\n" + "=" * 60)
    print("EJEMPLO INTERACTIVO")
    print("=" * 60)
    
    # Ejemplo interactivo
    try:
        entrada = input("\nIngresa números separados por comas para ordenar: ")
        numeros = [int(x.strip()) for x in entrada.split(",")]
        
        print(f"\nLista original: {numeros}")
        quicksort(numeros)
        print(f"Lista ordenada: {numeros}")
        
    except ValueError:
        print("Error: Ingresa solo números enteros separados por comas.")
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.")