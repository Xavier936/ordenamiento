def validarCedula(cedula):
    #se comprueba que  pertenezca a una provincia
    prov = int(cedula[:2])
    if prov > 0 and prov <=24:
        d = [0,0,0,0,0,0,0,0,0,0]
        #d[i] = int(cedula[i])
        for i in range(10):
            d[i] = int(cedula[i])
            #verificamos que el ultimo digito sea valido
            impar = 0
            par = 0
            #suma de posisciones impares
            for i in range(0, len(d), 2):

                val = d[i]*2

                if val > 9:
                    d[i] = val - 9
                    print("valores ", d[i])
                else:
                    d[i]= val
                
                impar =  impar + d[i]    
                
        
            #suma de posiciones pares
            for i in range(1,len(d)-1, 2):
                par = par + d[i]
            #print(" el valor es: ",par)
            
            st = par + impar

            tmp_1 = int(st) + 10
            tmp_1 = str(tmp_1)

            d10 = int(tmp_1[0:1]+"0")-st

            #if d10==10:
             #   d10 = 0
            #else:
             #   d10 = d10
            
            

        print("Ultimo digito ",d10)
        print(" el valor de poscicion impar es: ",impar)
        print(" el valor de posicicion par es: ",par)
        #print("pertenece a una provincia")
        #print(d)
        #print(type(d))
    else:
        print("no corresponde")



ci = input("Digite el nro de cédula: ")
validarCedula(ci)


