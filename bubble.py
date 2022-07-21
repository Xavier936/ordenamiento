def ordenamientoBurbuja(lista):
    #pivote se declara en True para asegurar que el bucle
    #se ejecute almenos una vez
    pivote = True
    while pivote:
        pivote = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i +1]:
                #Intercambio de datos
                lista[i], lista[i + 1] = lista[i +1], lista [i]
                pivote = True



listaNumeros = [2,9,5,8,12,4,7,25]

ordenamientoBurbuja(listaNumeros)

print(listaNumeros)
