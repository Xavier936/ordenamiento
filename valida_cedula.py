#from operator import add


def validarCedula(cedula):
    #se verifica que los dos primeros correspondan a una provincia
    prov = int(cedula[0:2])

    if not (prov> 0 and prov <= 24):
        
        return False
    
    #verifica que el ultimo digito sea valido

    d = [0,0,0,0,0,0,0,0,0,0]

    #se asigna el string a un array

    for i in range(10):
        d[i] = int(cedula[i])
    
    imp = 0
    par = 0

    #se suma los duplos de pos impar

    for i in range(0, len(d), 2):
        if (d[i]*2) > 9:
            d[i] = (d[i]*2) -9
        else:
            d[i] =(d[i]*2)
        imp = imp + d[i]

    #se suma las posiciones par
    for i in range(0, len(d)-1, 2):
        par = par + d[i]

    #se suma impar + par

    suma = imp + par

    #restamos la decena superior
    tmp_1= int(suma)+10
    tmp_1 = str(tmp_1)

    d10 = int(tmp_1[0:1] + "0")-suma

    #si es diez el digito es 0
    if d10 == 10:
        d10 = 0
    else:
        d10 = d10
    #si el decimo digito calculado es igual al digitado la cedula es correcta

    if d10 == d[9]:
        print("Cedula valida")
        return True
    else:
        print("Cedula no valida")
        return False



validarCedula("0202026886")