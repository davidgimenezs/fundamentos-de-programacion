def verificar_armstrong(numero):
    cadena_numero = str(numero)
    cantidad_digitos = len(cadena_numero)
    suma_potencias = sum(int(digito) ** cantidad_digitos for digito in cadena_numero)
    return suma_potencias == numero

def verificar_perfecto(numero):
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

n = 1
acu_armstrong = 0
acu_perfecto = 0

while n > 0 and n <= 1000:
    n = int(input())
    if n < 1 or n > 1000:
        break
    
    if verificar_armstrong(n):
        acu_armstrong += 1
    
    if verificar_perfecto(n):
        acu_perfecto += 1

print(acu_armstrong, acu_perfecto)