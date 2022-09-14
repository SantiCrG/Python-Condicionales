cantidad = int(input("Digite la cantidad de productos comprados: "))

if cantidad > 0:

    total = cantidad * 100000

if 5 >= cantidad <= 10:
    total *= 0.5
elif cantidad >=10:
    total*= 0.8
elif cantidad <= 100:
    total *= 0.8
elif cantidad <=5:
    print("No hay descuento", total)


print("El total a pagar es de ${}" .format(total))



 