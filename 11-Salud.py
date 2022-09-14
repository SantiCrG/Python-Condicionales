peso = float(input("Escriba su peso (kg): "))
talla = float(input("Escriba su estatura (m)"))

total = peso / talla**2

if total <= 20:
    print("Desnutrido")
elif total >=20:
    print("Normal")
elif total == 25 and 30:
    print("Sobrepeso")
elif total == 35 and 40:
    print("Obesidad Grado 1")
elif total == 35 and 40:
    print("Obesidad Grado 2")
elif total >= 40:
    print("Obesidad Grado 3")