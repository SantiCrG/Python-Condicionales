from __future__ import print_function
from wsgiref.validate import validator

print("******************************")
print("BIENVENIDO A CARROSPORTS")
print("******************************")

valor = int(input(" ¿Cuantas llantas llevara?: "))

if valor <= 5:
    print("El precio es de $240.000")
elif valor == 6 and 7:
    print("El valor es de $221.000")
elif valor >=7:
    print("El precio es de $180.000")