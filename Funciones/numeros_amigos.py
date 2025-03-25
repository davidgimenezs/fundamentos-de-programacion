def suma_divisores_propios(n):
    suma = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            suma += i
    return suma

def verificar_numeros_amigos(a, b):
    return suma_divisores_propios(a) == b and suma_divisores_propios(b) == a

while True:
    a = input().strip()
    b = input().strip()
    
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        
        if 100 < a < 32000 and 100 < b < 32000:
            if verificar_numeros_amigos(a, b):
                print("Son numeros amigos")
            else:
                print("No son numeros amigos")
            break
    else:
        pass
