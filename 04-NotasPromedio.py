from calendar import prmonth


not1 = int(input("Ingrese la nota 1 "))
not2 = int(input("Ingrese la nota 2 "))
not3 = int(input("Ingrese la nota 3 "))
not4 = int(input("Ingrese la nota 4 "))
not5 = int(input("Ingrese la nota 5 "))

promedio = (not1 + not2 + not3 + not4 + not5) / 5

if promedio >= 30:
    print(" !!Felicitaciones!! Aprobo, Con una nota de: ", promedio)
else:
    print("Lo siento NO aprobo, Con una nota de: ", promedio)
