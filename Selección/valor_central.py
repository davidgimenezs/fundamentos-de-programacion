a = int(input())
b = int(input())
c = int(input())

if (a > b and a > c):  # Si 'a' es el mayor
    if b > c:
        print(b)
    else:
        print(c)

elif (b > a and b > c):  # Si 'b' es el mayor
    if a > c:
        print(a)
    else:
        print(c)

else:  # Si 'c' es el mayor
    if a > b:
        print(a)
    else:
        print(b)

#segundo_mayor = sorted([a, b, c])[1]
#print(segundo_mayor)