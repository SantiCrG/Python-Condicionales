from turtle import colormode


colombia = int(input("Ingrese el numero: "))
# Se divide entre dos para saber si es par o impar
if colombia == 0:
    print("El numero es cero")
elif colombia %2 == 0:
    print("El numero es impar")
else:
    print("El numero es par")