cuenta = int(input("Ingrese el valor total de la deuda: "))

if cuenta <= 150000:
    print("Su pago se realizara en efectivo")
elif cuenta <= 300000:
    print("Su pago se realizara en nequi")
elif cuenta >= 600000:
    print("Su pago se realizara en debito")
else:
    print("Su pago se realizara en credito")