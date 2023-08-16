#ejercicio conversor temperatura#

temperatura=float(input("Ingrese la temperatura: "))
escala=input("Farenheit (F), Celsius (C)").upper()

if escala=="F":
    celsius=(temperatura-32)*5/9
    print("Temperatura en celsius es: "+str(celsius))
elif escala=="C":
    farenheit=(temperatura*1.8) +32
    print("Temperatura en farenheit es: "+str(farenheit))
else:
    print("No existe escala")

