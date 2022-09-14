from pickletools import OpcodeInfo
from sqlite3 import IntegrityError


pizza = """
Eliga el tamaño de pizza que desea
(1)-Tamaño 1
(2)-Tamaño 2
(3)-Tamaño 3
"""
opcion = input(pizza)
ingre = int(input("Cuantos ingredientes desea llevar, Escribir 0 si ninguno")) 
ingre = 4000 * ingre
if opcion == "1":
    total = 15000 + ingre
    print("el total es de : ", total)
elif opcion == "2":
    total2 = 24000 + ingre
    print("El total es de", total2 )
elif opcion == "3":
    total3 = 36000 + ingre
    print("El total es de ", total3 )
