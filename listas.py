#Listas#
lenguajes=["Java","Ruby","PHP",".Net"]
print(lenguajes[1])
#lenguajes[1]="Go"
print(lenguajes)
print(lenguajes[-1]) #se refiere al ultimo elemento desde el final hasta el inicio
print(lenguajes[1:3]) #imprime un rango de la lista

lenguajes.insert(3,"Go")
lenguajes.insert(0,"C")
lenguajes.remove("PHP")
print("Ruby" in lenguajes)
print(len(lenguajes))
print(lenguajes)