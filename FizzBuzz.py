def fizz():
    numeros = []
    for i in range(1,100):
        if i %15 == 0:
            i = 'fizzBuzz'
        elif i %3 == 0:
            i = 'fizz'
        elif i % 5==0:
            i = 'buzz'
        else:
            numeros.append(str(i))
            print(numeros)




fizz()