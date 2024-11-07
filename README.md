# pr3_1184_GomezGarcia_Python

print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")
#Se le pide al usuario su edad
edad=int(input("Escriba su edad: "))

#Si edad es menor o mayor a 18 imprimira un mensaje distinto en cada caso 
if edad<18:
    print("Usted no es mayor de edad")
elif edad>=18:
    print("Usted es mayor de edad")


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




print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

#Declara una lista
frutas=["Platano","Frambuesa", "Manzana", "Cereza"]

#Si la cereza esta en la lista imprimira un mensaje si no imprimira otro mensaje
if "Cereza" in frutas:
    print("Cereza se encuentra en la lista")
else:
    print("Cereza no esta en la lista")

print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

#Declara lista
nombre_apellido=["Noe", "Gael", "Gomez", "Garcia"]

#Imprime solo los apellidos
print(nombre_apellido[2], nombre_apellido[3])


print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

#La variable que guardará la suma
suma = 0

#Usamos range para obtener solo los números pares entre 2 y 100
for i in range(2, 101, 2):  #El tercer parámetro (2) es el paso, que hace que se tome solo los pares
    suma += i

#Imprime el resultado
print("La suma de los números pares entre 2 y 100 es:", suma)



print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")


# Define un numero
numero = 7

# Usar un bucle for con un rango de 1 a 10 para imprimir la tabla
for i in range(1, 11):  # El rango va de 1 a 10 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

# Definir una lista
mi_lista = [10, 20, 30, 40, 50]

# Usar un bucle for para recorrer e imprimir los elementos de la lista
for elemento in mi_lista:
    print(elemento)


print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

#Define una lista
mi_lista = [10, 20, 30, 40, 50]

#Inicia un índice
indice = 0

#Usa un bucle while para recorrer la lista
while indice < len(mi_lista):
    print(mi_lista[indice])  #Imprime el elemento en la posición indicada
    indice += 1  



print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

# Definir la cadena de texto
cadena = "Hola soy Noe de 3°W"

# Usar un bucle for para recorrer e imprimir cada carácter
for caracter in cadena:
    print(caracter)



print(" ")
print("Gomez Garcia Andres Noe 1184: Practica 3")
print(" ")

# Parte ascendente
for i in range(1, 6):  # De 1 a 5
    print('*' * i)

# Parte descendente
for i in range(4, 0, -1):  # De 4 a 1
    print('*' * i)
