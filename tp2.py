#1) Pida un número al usuario y determine si es par o impar.

"""numero=input("ingrese numero:")
numero=int(numero)

if numero%2==0:
    print("es par")
else:
    print("es impar")"""

#2) Escriba una cadena if-elif-else que determine el estado de vida de una persona.
#• Si la persona tiene menos de 2 años, muestre un mensaje que diga que es un bebe.
#• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
#• Si tiene al menos 4, pero menos de 12, muestre que es un niño.
#• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
#• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
#• Si tiene 65 o más, muestre que es un anciano."""

"""edad=input("ingrese edad: ")
edad=int(edad)

if edad<2:
    print("es un bebe")

elif 1<edad<4:
    print("es un infante")

elif 3<edad<12:
    print("es un niño")

elif 12<edad<20:
    print("es un adolescente")

elif 19<edad<65:
    print("es un adulto")

else:
    print("es un anciano")"""



#3) Cree un ciclo que nunca termine y ejecútelo. Puede probarlo haciendo que muestre algo en pantalla por cada pasada del ciclo. Para finalizarlo, presione Ctrl-C o el comando para detener la ejecución correspondiente a su editor
   
"""palabra=input("escribir algo:")
while True:
        print("hola")"""


#4) Escriba un programa que contenga dos ciclos while anidados que muestre los enteros del 1 al 100, diez números por línea.


"""numeros_enteros= 1
fila=10
columna=10

for i in range(fila):
    for j in range(columna):
        print(numeros_enteros, " ", end="")
        numeros_enteros+=1
    print()"""

#5) Resuelva el ejercicio anterior usando solo un ciclo while
"""contador=1
elementos_por_linea=0
while contador <= 100:
    print(contador, " ", end="")
    elementos_por_linea += 1  
    contador+=1
    if elementos_por_linea == 10:
        print()  
        elementos_por_linea = 0"""