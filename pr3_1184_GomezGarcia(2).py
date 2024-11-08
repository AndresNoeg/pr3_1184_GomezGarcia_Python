print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

#Se le pide al usuario su Calificacion
califa=float(input("Escriba su calificacion: "))

#Dependiendo de la calificacion imprimira un mensaje u otro
if califa>=0 and califa<5:
    print("Suspendiste")
elif califa>=5 and califa<6:
    print("Suficiente")
elif califa>=6 and califa<7:
    print("Bien")
elif califa>=7 and califa<9:
    print("Notable")
elif califa>=9 and califa<=10:
    print("Sobresaliente")