
from distutils.command.install_scripts import install_scripts




rusia = """
Seleccione una Opcion
(1)-Area Cuadrado
(2)-Area Rectangular
(3)-Area Circulo
"""
# opcion = int(input(rusia))
opcion = input(rusia)

if opcion == "1":
    lado = int(input("Ingrese el valor del lado (cm): "))
    area_c = lado * lado
    print("El area del cuadrado es: ", area_c)
elif opcion == "2":
    dass = int(input("Ingrese el valor del lado : "))
    porqueno = dass * dass
    print("El area del rectangulo es", porqueno)

