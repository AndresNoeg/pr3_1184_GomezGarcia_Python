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