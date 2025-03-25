dia = input()
mes = input()
anho = input()

if not dia.isdigit() or not mes.isdigit() or not anho.isdigit():
    print("No es una fecha valida!!")
else:
    dia = int(dia)
    mes = int(mes)
    anho = int(anho)

    if anho <= 0 or mes < 1 or mes > 12:
        print("No es una fecha valida!!")
    else:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_mes = 31
        elif mes in [4, 6, 9, 11]:
            dias_mes = 30
        else:
            if (anho % 4 == 0 and anho % 100 != 0) or (anho % 400 == 0):
                dias_mes = 29
            else:
                dias_mes = 28

        if dia < 1 or dia > dias_mes:
            print("No es una fecha valida!!")
        else:
            dia += 1
            if dia > dias_mes:
                dia = 1
                mes += 1
                if mes > 12:
                    mes = 1
                    anho += 1

            print(f"{dia}/{mes}/{anho}")
