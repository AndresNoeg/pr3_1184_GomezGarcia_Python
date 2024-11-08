print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

#Se le piden a los usuarios 4 calificaciones
l1=float(input("Ingrese una calificacion: "))
print(" ")
l2=float(input("Ingrese la segunda calificacion: "))
print(" ")
l3=float(input("Ingrese la tercera calificacion: "))
print(" ")
l4=float(input("Ingrese la cuarta calificacion: "))
print(" ")

#Se declara una lista y la imprime
califas=[l1,l2,l3,l4]
print(califas)
print("Las calificaciones se ordenaran de menor a mayor a  continuacion")
print(" ")
califas.sort()#Ordena las calificaciones de menor a mayor
print(califas) #Imprime las calificaciones ordenadas