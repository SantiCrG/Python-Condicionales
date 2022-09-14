from errno import EADDRNOTAVAIL
from functools import total_ordering
from pickletools import OpcodeInfo


menu = """
Eliga su genero
(1)- Femenino
(2)- Masculino
"""


opcion = input(menu)

if opcion == "1":
    edad = int(input("ingrese su edad "))
    total = (220 - edad)/10
    print("Sus pulsasiones son: ", total)
elif opcion == "2":
    edad2 = int(input("ingrese su edad "))
    total2 = (210 - edad2)/10
    print("Sus pulsasiones son: ", total2)