#solicitar al usuario que ingrese un número y, 
#si el número está en la lista, eliminar su primera ocurrencia. 
#Mostrar un mensaje si no es posible eliminar.

def eliminar(lista,nro):
    if nro in lista:
        lista.remove(nro)
    else:
        print("El numero no se encuentra en la lista")
    


numeros =[2,4,1,6,7,9,4]
print(numeros)
n = int(input("Ingrese el nro a eliminar: "))

eliminar(numeros,n)
print(numeros)
