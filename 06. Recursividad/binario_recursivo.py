def binario(numero):
    if numero < 2:
        print(numero, end="")
    else:
        binario(numero // 2)
        print(numero % 2, end="")

def validar():
    while True:
        entrada = input()
        if entrada.isdigit():
            return int(entrada)

nro = validar()
binario(nro)