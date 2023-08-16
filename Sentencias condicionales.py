#Sentencia if-else
"""nota_matematicas=int(input("Ingrese la nota de matemáticas: "))
nota_lenguaje=int(input("Ingrese la nota de lenguaje: "))
nota_biologia=int(input("Ingrese la nota de biologia: "))
promedio=int(nota_matematicas+nota_lenguaje+nota_biologia/3)
if promedio >= 6:
    print("Felicidades paso el año tu nota es de: ", promedio)
else:
    print("no paso")"""


#Sentencia elif

"""numero=int(input("Ingrese el número que desee convertir "))

if numero==1:
    print("El número es 'Uno'")
elif numero==2:
    print("El número es 'Dos'")
elif numero==3:
    print("El número es 'Tres'")
elif numero==4:
    print("El número es 'Cuatro'")
elif numero==5:
    print("El número es 'Cinco'")
else:
    print("El convertidor solo reconoce hasta el número 5")"""


print("Menú de opciones:\n")
print("1. Convertir de número a palabra\n")
print("2. Convertir de palabra a número\n")

opcion=int(input("Ingrese una opción: "))

if opcion==1:
    numero=int(input("Ingrese el número que desee convertir a palabra "))

    if numero==1:
        print("El número es 'Uno'")
    elif numero==2:
        print("El número es 'Dos'")
    elif numero==3:
        print("El número es 'Tres'")
    elif numero==4:
        print("El número es 'Cuatro'")
    elif numero==5:
        print("El número es 'Cinco'")
    else:
        print("El convertidor solo reconoce hasta el número 5")

elif opcion==2:

    texto=input("Ingrese la palabra para convertir a número ").lower()

    if texto=='uno':
        print("El número es '1'")
    elif texto=='dos':
        print("El número es '2'")
    elif texto=='tres':
        print("El número es '3'")
    elif texto=='cuatro':
        print("El número es '4'")
    elif texto=='cinco':
        print("El número es '5'")
    else:
        print("El convertidor solo reconoce hasta la palabra 'Cinco'")
else:
    print("La opción seleccionada no existe")
