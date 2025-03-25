caracter = str(input())

if caracter.islower() == True:
    print("El caracter ingresado es una letra (minuscula)")
    
elif caracter.isupper() == True:
    print("El caracter ingresado es una letra (mayuscula)")
    
elif caracter.isalpha() == False:
    print("El caracter ingresado NO corresponde a una letra")