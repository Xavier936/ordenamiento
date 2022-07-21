#Solicitar al usuario que ingrese números,
#los cuales se guardarán en una lista. 
# Finalizar al ingresar el número 0, 
# el cual no debe guardarse.

numeros=[]

n = int(input("Ingrese un numero: "))

while n != 0:
    numeros.append(n)#añadiendo los numeros en la lista
    n = int(input("Ingrese otro numero: "))
    if n == 0:
        print("La lista ingresada es: ")
        print(numeros)
    