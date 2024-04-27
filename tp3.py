#1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo para un rango de números indicado por un usuario.

"""lista=[]
for i in range(1,21):
    lista.append(i)
print(lista)

lista2=[]
limiteinf=int(input("ingrese limite inferior: "))
limitesup=int(input("ingrese limite superior: "))

for i in range(limiteinf,limitesup+1):
    lista2.append(i)
print(lista2)"""


#2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. 

"""lista3=[]
numero=int(input("ingrese un numero: "))
for i in range(numero*1,numero*11,numero):
    lista3.append(i)
print(lista3)"""

#3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir caracteres.

"""lista_sin_repeticion=[]
oracion=input("ingrese oracion: ")
for caracter in oracion:
    if caracter not in lista_sin_repeticion:
        lista_sin_repeticion.append(caracter)
print(lista_sin_repeticion)"""

#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.

"""lista_sin_espacios=[]
palabras=input("ingrese oracion: ")
for caracter in palabras:
    if caracter!=" ":
        lista_sin_espacios.append(caracter)
print(lista_sin_espacios)"""

#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

"""tupla=(1,2,3,4,5,1,1,2,4)
variable=input("ingrese numero: ")
contador=0
variable=int(variable)

for elemento in tupla:
   if elemento==variable:
     contador=contador+1
print(contador)"""


#6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero

"""tupla_meses=("x","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
indice=int(input("ingrese numero: "))

if indice==0: print("numero invalido")
elif indice>12: print("numero invalido")
else: print(tupla[indice])"""

#7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga.

"""tupla_num=(15,20,1,100,30,5,26)
mayor_valor=tupla_num[0]
menor_valor=tupla_num[0]

for numero in tupla_num:
    if numero<menor_valor: menor_valor=numero
    elif numero>mayor_valor: mayor_valor=numero

print(tupla_num)
print("el numero con mayor valor es:", mayor_valor)
print("el numero con menor valor es: ", menor_valor)"""

#8) (Opcional)Escribir un programa que vaya solicitando al usuario que ingrese nombres. - Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. - Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena "*", para salir del programa

"""agenda={"Sofia":3875555444, "Martin":3879997777, "Agustin":3876588754, "Maria":3879879645, "Luis":3876652621, "Valentina":3876453621, "Juan":3513827112, "Guillermo":3512637818, "Renata":3517283948}

while True:
    nombre=input("ingrese un nombre: ")
    
    if nombre=="*":
        print("saliendo del programa")
        break

    elif nombre in agenda: 
        print(agenda[nombre])
        cambiar=input("¿el numero es correcto?: ")

        if cambiar=="no":
            nuevo_numero=input("ingrese el numero correcto: ")
            agenda[nombre]=nuevo_numero   
    
        else: break

    else:    
        print("ese nombre no se encuentra en la agenda")
        numero=input("ingrese el numero no encontrado: ")
        agenda[nombre]=numero"""
    

#9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor
lista=[]
lista_ordenada=[]
while True:
    numero=int(input("ingrese un numero: "))
    lista.append(numero)
    for i in range (len(lista )):
        for j in range(i+1, len(lista)):
         if lista[j]<lista[i]:
            aux=lista[j]
            lista[j]=lista[i]
            lista[i]=aux
    if  numero==0:
        break
print(lista)

#10) Opcional: Lo mismo que el anterior, pero ordenando de mayor a menor.
#11) Opcional: Codificador Morse: Desarrolle un programa en Python que permita al usuario escribir un mensaje y convertirlo a código Morse.

"""codigo_morse={"a":".-","b": "-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"--","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
mensaje=input("ingrese un mensaje: ")

mensaje_en_codigo= ""
for caracter in mensaje:
    if caracter in codigo_morse:
        mensaje_en_codigo += codigo_morse[caracter] + " "

print(mensaje_en_codigo)"""



