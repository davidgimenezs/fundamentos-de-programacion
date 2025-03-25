def cifrar_numero(N):
    N_str = str(N)
    N_cifrado = []
    
    for digit in N_str:
        d = int(digit)
        cifrado = (d + 7) % 10
        N_cifrado.append(str(cifrado))
    
    return ''.join(N_cifrado)

while True:
    N = input().strip()
    if N.isdigit() and int(N) > 0:
        N = int(N)
        N_cifrado = cifrar_numero(N)
        print(N_cifrado)
        break
    else:
        pass
