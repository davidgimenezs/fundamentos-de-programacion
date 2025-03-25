def es_entero(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

entrada = input()

if not es_entero(entrada):
    print("Error: entrada no válida")
else:
    numero = int(entrada)
    es_negativo = numero < 0
    if es_negativo:
        numero = -numero

    numero_invertido = 0
    while numero > 0:
        numero_invertido = numero_invertido * 10 + numero % 10
        numero //= 10
    
    if es_negativo:
        numero_invertido = -numero_invertido
    
    print(numero_invertido)
