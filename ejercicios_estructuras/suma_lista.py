#Recorrer la lista para imprimir la sumatoria de todos los elementos.

def sumatoria(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

numeros = [2,4,1,5,3]
print(numeros)

print("la sumartoria de la lista es:", sumatoria(numeros))