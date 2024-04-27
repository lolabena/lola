def numprimo(numero):
    if numero<=1:
        return False
    
    for i in range(2, numero):
        if numero%i==0:
            return False
    return True

def primosAyB(limiteinf, limitesup):
    lista=[]
    for i in range (limiteinf,limitesup):
        if numprimo(i):
            lista.append(i)
    return lista

print(primosAyB(2,30))