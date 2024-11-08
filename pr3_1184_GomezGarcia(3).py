print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

#Se le pide al usuario un apellido un un nombre
nombre=str(input("Ingrese un nombre: "))
apellido=str(input("Ingrese un apellido: "))

#Dependiendo si el usuario uso el nombre y apelllido corrrectos imprimira un mensaje u otro
if nombre=="Daniel" and apellido=="Ramos":
    print(nombre, apellido)
elif nombre=="Daniel" and apellido != "Ramos" :
    print("Apellido incorrecto ")

elif nombre != "Daniel" and apellido == "Ramos" :
    print("Usuario desconocido")
else:
    print("Error...")