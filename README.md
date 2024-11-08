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

![image](https://github.com/user-attachments/assets/a5aaf567-aa80-468e-9c8a-9d0f5cc976d6)

![image](https://github.com/user-attachments/assets/6cc8ac2e-cfb1-4474-933c-d9dc2729152d)




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

![image](https://github.com/user-attachments/assets/f5b81c97-725b-4004-a093-de1b0452cb70)

![image](https://github.com/user-attachments/assets/88529118-9eb1-4d04-954d-0c04a69e4fe6)

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

![image](https://github.com/user-attachments/assets/03ecab32-5a04-4c3e-9d86-0b9ba61fa5d5)

![image](https://github.com/user-attachments/assets/df77ac7a-0530-4804-b737-2594d08c80ac)

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

![image](https://github.com/user-attachments/assets/9c574e7b-17cf-49f2-9228-217ba25ab701)

![image](https://github.com/user-attachments/assets/ce2467c7-9691-468d-8f12-835e5c3ea835)

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

![image](https://github.com/user-attachments/assets/6cf98018-a38b-407b-bc61-8e018f1ebe65)

![image](https://github.com/user-attachments/assets/19499764-e115-4a95-93c3-136718abf1f5)

print(" ")

print("Gomez Garcia Andres Noe 1184: Practica 3")

print(" ")

#Declara lista

nombre_apellido=["Noe", "Gael", "Gomez", "Garcia"]


#Imprime solo los apellidos

print(nombre_apellido[2], nombre_apellido[3])

![image](https://github.com/user-attachments/assets/ca238328-0c7c-434b-a553-7730d16e9d20)

![image](https://github.com/user-attachments/assets/05473474-a148-4edf-9aa5-c6b11215096a)


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

![image](https://github.com/user-attachments/assets/1cb56dc7-70ca-476e-8304-a7c8b8d7f70f)}

![image](https://github.com/user-attachments/assets/37b7c5e5-e239-4dd6-b6cb-a668dd6994e6)

print(" ")

print("Gomez Garcia Andres Noe 1184: Practica 3")

print(" ")


# Define un numero

numero = 7

# Usar un bucle for con un rango de 1 a 10 para imprimir la tabla

for i in range(1, 11):  # El rango va de 1 a 10 

    resultado = numero * i
    
    print(f"{numero} x {i} = {resultado}")

![image](https://github.com/user-attachments/assets/92c5aa9b-8135-464f-9c8a-22a4a818c657)

![image](https://github.com/user-attachments/assets/b8c22465-714d-4f41-b67d-8e2c5dffdc36)

print(" ")

print("Gomez Garcia Andres Noe 1184: Practica 3")

print(" ")

# Definir una lista

mi_lista = [10, 20, 30, 40, 50]

# Usa un bucle for para recorrer e imprimir los elementos de la lista

for elemento in mi_lista:

    print(elemento)

![image](https://github.com/user-attachments/assets/f65bf3ee-c7ec-4be5-b470-c86e3e0dfbfd)

![image](https://github.com/user-attachments/assets/47835e0b-5890-4dc7-a2e2-d5ee5c28fd13)

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
![image](https://github.com/user-attachments/assets/3bd332d7-17ff-4a58-a641-17e01b38d1cb)

![image](https://github.com/user-attachments/assets/9e82ec01-05f1-49d5-b35d-e35936704346)

print(" ")

print("Gomez Garcia Andres Noe 1184: Practica 3")

print(" ")

# Definir la cadena de texto

cadena = "Hola soy Noe de 3°W"

# Usar un bucle for para recorrer e imprimir cada carácter

for caracter in cadena:

    print(caracter)

![image](https://github.com/user-attachments/assets/00a8a046-0b9a-4f31-a84c-db775f674444)

![image](https://github.com/user-attachments/assets/e88a22cf-06d2-4aad-b176-63f14e5e8e43)

print(" ")

print("Gomez Garcia Andres Noe 1184: Practica 3")

print(" ")

# Parte hacia arriba

for i in range(1, 6):  # De 1 a 5

    print('*' * i)

# Parte hacia abajo

for i in range(4, 0, -1):  # De 4 a 1
    print('*' * i)

![image](https://github.com/user-attachments/assets/7db7e6c0-cc9b-4642-8f5f-a6e129113287)

![image](https://github.com/user-attachments/assets/df05067c-38c7-42b7-b501-f9a81ab6c837)


