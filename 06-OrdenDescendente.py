val1 = int(input("Ingrese el primer numero: "))
val2 = int(input("Ingrese el segundo numero: "))
val3 = int(input("Ingrese el tercer numero: "))

if(val1>val2 and val2>val3):
    print(" ",val1,"  ", val2, "  ", val3)
elif(val2>val1 and val1>val3):
    print(" ",val2," ",val1," ",val3)
elif(val3>val1 and val1>val2):
    print(" ",val3," ",val1," ",val2)
