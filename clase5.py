"""def Saludar():
    print("hola")
Saludar()

def Sumar2numeros(numero1,numero2):
    print(numero1+numero2)

Sumar2numeros(1,2)"""

#1.escriba una función que muestre todos los numeros primos entre 1 y un número n que es ingresado por parametro

def Esprimo(numero):
    if numero<=1:
        return False
    for i in range(2, numero):
        if numero%i==0:
            return  False
    return True

def Primosdel1_N(N):
    for i in range(1,N+1):
        if Esprimo(i):
            print(i)

Primosdel1_N(1000)

#2.soliccitar al usuario que ingrese su direccion email.Imprimir un mensaje indicando si la dirección es válida o no, valiendose de una función para decirlo. Una direccion se considerará válida si contiene el símbolo @.

def Validez(email):
    for caracter in email:
        if caracter=="@":
            return True
        else: return False
email=input("ingrese email: ")

if Validez(email):
    print("es valido")
else: print("es invalido")

#