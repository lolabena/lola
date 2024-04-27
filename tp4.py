#1. Diseña una función que tome como parámetro 2 números, y que devuelva una lista que contenga TODOS los números enteros entre estos 2 incluyendo AMBOS parámetros.

"""def lista_numeros_enteros(inicio, fin):
    numeros_enteros = []
    for num in range(inicio, fin + 1):
        numeros_enteros.append(num)
    return numeros_enteros
inicio=int(input("inicio: "))
fin=int(input("fin: "))

print(lista_numeros_enteros(inicio, fin))"""

#2. Escribir una función que tome como parámetro 2 números, y retorne una lista con todos los números pares entre estos, EXCLUYENDO a los parámetros.

"""principio= int(input("ingrese numero:"))
final=int(input("ingrese numero: "))

def lista_pares (principio, final):
    numeros_pares=[]
    for numeros in range(principio+12, final):
        if  numeros%2==0:
            numeros_pares.append(numeros)
    return numeros_pares

print(lista_pares(principio, final))"""


#3. Escribir una función que tome 2 parámetros, el primero que reciba una cadena, y el segundo que reciba un carácter. La función tendrá que retornar la cantidad de veces que aparece ese carácter en esa cadena.

"""cadena=input("ingrese cadena: ")
caracter=input("ingrese caracter: ")

def caracter_cadena (cadena, caracter):
    contador=0
    for car in cadena:
        if car==caracter:
            contador+=1
    return contador

print(caracter_cadena(cadena, caracter))"""


#4. Elaborar una función que tome como parámetro 2 números, y retorne una lista con todos los números primos entre ese rango de números.


#5. Elaborar una función que tome como parámetro una lista, y devuelva un bool que diga si en esa lista TODOS sus números son pares.
"""lista=[3,4,5,6,7,8,9,10]
def todos_pares(lista):
    for num in lista:
        if num % 2 != 0:  
            return False  
    return True  

print(todos_pares(lista))"""

#6. Elaborar una función que tome como parámetro una lista y devuelva un bool que diga si en esa lista TODOS sus números son primos.

listaprimos=[17,23,11,13]
             
def Esprimo(listaprimos):
    for i in listaprimos:
        if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            return False
    return True

print(Esprimo(listaprimos))
        


