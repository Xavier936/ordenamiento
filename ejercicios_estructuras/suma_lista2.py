#juntar ejercicio 1 y 3

def Ingreso(lista,nro):
    while nro != 0:
        lista.append(nro)
        nro = int(input("Ingrese otro numero: "))
        if nro == 0:
            print("La lista ingresada es: ")

def sumatoria(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

numeros = []
num = int(input("Ingrese un numero: "))
Ingreso(numeros,num)
print(numeros)
print("la sumatoria de la lista es:", sumatoria(numeros))
