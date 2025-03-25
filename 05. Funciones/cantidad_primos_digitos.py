
#Función que devuelve el resultado de a^b.
#Se supone que b es un número no-negativo.*/
def potencia(a, b):
    return a ** b
    
#Función que devuelve true si el número n es primo, y false en caso contrario.
#Se supone que n es positivo.*/
def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
#Función que devuelve la cantidad de dígitos de un número n.
#Se supone que n es positivo.*/
def cantDigitos( n):
    return len(str(n))

#Función solicitada para el problema planteado.*/
#completar*/ cantNoPrimos_C_Digitos(/*completar*/)
#    //Escribir
#    //aquí
#    //la solución
def cantNoPrimos_C_Digitos(N, C):
    digitos = str(N)
    total_digitos = len(digitos)
    
    if C > total_digitos:
        return -1
    
    no_primos = 0
    
    for i in range(total_digitos - C + 1):
        num = int(digitos[i:i+C])
        if not esPrimo(num):
            no_primos += 1
    
    return no_primos



N=int(input())
C=int(input())
print("Cantidad de no-primos de ",C," digitos: ",cantNoPrimos_C_Digitos(N,C));