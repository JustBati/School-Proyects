import random
import time
#genera las cadenas de bits aleatoriamente
def Gene():
    x = format(random.randint(0, 8) ,"b")#pasa binario
    if (len(x)<4):#comprueba que la cadena tenga la cantidad deseada de bits
        for j in range(4-len(x) ):#agrega 0s en una cadena a concatenar
            c=''
            if (j == 0):
                    c = "0"
            else:
                c = c + "0"    
        
            x = c + x
    return x

def Paridad(cadena):
    q='0'
    for j in cadena:
        if(q=='0' and j=='0'):
            q='2'
           # print("primer estado\n")
        elif(q=='0' and j=='0'):
            q='1'
            #print("primer estado\n")

        elif(q=='1' and j=='0'):
            q='3'
            #print("Segundo estado\n")
        elif(q=='1' and j=='1'):
            q='0'
           # print("Segundo estado\n")

        elif(q=='2' and j=='1'):
            q='3'
           # print("Tercer estado\n")
        elif(q=='2' and j=='0'):
            q='0'
           # print("Tercer estado\n")
    
        elif(q=='3' and j=='1'):
            q='2'
           # print("Cuarto estado\n")
        elif(q=='3' and j=='0'):
            q='0'
          #  print("Cuarto estado\n")
    return q

                         #generando las cadenas

pro= open("Protocolo.txt", "w")
acepta= open("asdf.txt", "w")
recha= open("rechasasda.txt", "w")  #abriendo archivo
for i in range(5):                    #moviendonos por cadenas
    sec=Gene()
    pro.write(f"{sec} ")
    estado =Paridad(sec)
    if (estado=='0'):
        acepta.write(f"{sec} ")
    else:
        recha.write(f"{sec} ")
    print(f"{sec}      {estado}")
pro.close()
acepta.close()
recha.close()


        