#Sentencia if-else
nota_matematicas=int(input("Ingrese la nota de matemáticas: "))
nota_lenguaje=int(input("Ingrese la nota de lenguaje: "))
nota_biologia=int(input("Ingrese la nota de biologia: "))
promedio=int(nota_matematicas+nota_lenguaje+nota_biologia/3)
if promedio >= 6:
    print("Felicidades paso el año tu nota es de: ", promedio)
else:
    print("no paso")


