def operaciones(lista):
    numeros = []
    for i in lista:
        if i == '+':
            numeros.append(numeros[-1] + numeros[-2])
        elif i == 'C':
            numeros.pop()
        elif i == 'D':
            numeros.append(2* numeros[-1])
        else:
            numeros.append(int(i))
    print(sum(numeros))



ops = ["5","-2","4","C","D","9","+","+"]
operaciones(ops)