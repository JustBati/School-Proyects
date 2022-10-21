import random
import matplotlib.pyplot as plt
import numpy as np
"""
Funcion que genera los universos binarios de n
y a su vez los guarda en un archivo llamado zn
-Regresa lista con la cantidad de 1's por cadena
"""

def  Univer(n):
    fic = open(f"z{n}.txt", "w")
    fic.write(f"z{n}="+"{e ")
    unos=[]
    for i in range(n): #aqui se hace la sumatoria de zigma Zf=Z1+Z2+...+Zn
        m = 2**(i+1) #numero maximo a calcular con i cantidad de bits
        for p in range(m):#for para calcular los numeros posibles
            x = format(p ,"b")#pasa binario
            if (len(x)<len(format(m, "b"))-1):#comprueba que la cadena tenga la cantidad deseada de bits
                for j in range(len(format(m ,"b"))-len(x) ):#agrega 0s en una cadena a concatenar
                    c=''
                    if (j == 0):
                     c = "0"
                    else:
                        c = c + "0"    
        
                x = c + x
           

            fic.write(f"{x} ")
    fic.write("}")
    fic.close()
    

def grafica():
    unos=[]
    n=int(input("n-->"))
    for i in range(n): #aqui se hace la sumatoria de zigma Zf=Z1+Z2+...+Zn
        m = 2**(i+1) #numero maximo a calcular con i cantidad de bits
        for p in range(m):#for para calcular los numeros posibles
            x = format(p ,"b")#pasa binario
            if (len(x)<len(format(m, "b"))-1):#comprueba que la cadena tenga la cantidad deseada de bits
                for j in range(len(format(m ,"b"))-len(x) ):#agrega 0s en una cadena a concatenar
                    c=''
                    if (j == 0):
                        c = "0"
                    else:
                        c = c + "0"    
            
                x = c + x
            unos.append(x.count('1'))


    plt.scatter(np.array(range(len(unos))), unos)
    unos.clear
    plt.show()



op=0
unos=[]
while op !=4:
    print("1-Numero aleatorio en un rango de 0 a 1000")
    print("2- Numero ingresado por el usuario")
    print("3- Grafica de los 1's existentes en n universo\n4-Salir\n")
    op =int(input("Elija la opcion deseada:\t"))

    if op==1:
        n = random.randint(0,1000) #n para zigma
        Univer(n)
        print(f"El fichero con el universo {n}, ha sido creado correctamente \n")
    elif op==2:
        n = (int(input("n -->")))#n para zigma
        Univer(n)
        print(f"El fichero con el universo {n}, ha sido creado correctamente \n")
    elif op==3:
        grafica()
        

