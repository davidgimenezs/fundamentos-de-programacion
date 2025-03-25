def rotar_lista(lista):
    nueva_lista = []
    nueva_lista.append(lista[len(lista)-1])
    for i in range(len(lista)-1):
        nueva_lista.append(lista[i])
    return nueva_lista

n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
    
resultado = rotar_lista(lista)

for i in range(len(resultado)):
    print(resultado[i], end=" ")