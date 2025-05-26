def invertir(numero):
    return int(str(numero)[::-1])

def validar():
    while True:
        entrada = input()
        if entrada.isdigit():
            return int(entrada)

numero = validar()
print(invertir(numero))