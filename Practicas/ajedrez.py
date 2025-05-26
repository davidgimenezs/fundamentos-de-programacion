def validar_entrada(posicion):
    if len(posicion) != 2:
        return False
    letra = posicion[0].lower()
    numero = posicion[1]
    
    if letra not in 'abcdefgh':
        return False
    if numero not in '12345678':
        return False
    return True

def obtener_posicion(posicion):
    letra = posicion[0].lower()
    numero = int(posicion[1])
    
    columna = ord(letra) - ord('a')
    fila = numero - 1
    
    return fila, columna

def calcular_movimientos(fila, columna):
    movimientos = []
    
    for i in range(8):
        if i != fila:
            movimientos.append((i, columna))
    
    for j in range(8):
        if j != columna:
            movimientos.append((fila, j))
    
    return movimientos

def crear_matriz(fila_torre, columna_torre, movimientos):
    matriz = []
    for i in range(8):
        fila = []
        for j in range(8):
            if i == fila_torre and j == columna_torre:
                fila.append('T')
            elif (i, j) in movimientos:
                fila.append('*')
            else:
                fila.append('-')
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for i in range(7, -1, -1):
        fila_str = ' '.join(matriz[i])
        print(fila_str)

def main():
    while True:
        entrada = input("Ingrese la posicion de la torre en el tablero: ")
        
        if not validar_entrada(entrada):
            print("Entrada invalida. Use formato como 'a1', 'h8', etc.")
            continue
        
        fila, columna = obtener_posicion(entrada)
        movimientos = calcular_movimientos(fila, columna)
        matriz = crear_matriz(fila, columna, movimientos)
        
        print("Los movimientos posibles para la torre son:")
        imprimir_matriz(matriz)
        break
    
main()