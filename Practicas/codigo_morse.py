morse_numeros = {
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
}

entrada = input().strip()

numeros_codificados = entrada.split("   ")

resultado = []
for grupo in numeros_codificados:
    digitos = grupo.split(" ")
    numero = ''.join([morse_numeros[d] for d in digitos])
    resultado.append(numero)

print(' '.join(resultado))
