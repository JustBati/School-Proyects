import matplotlib.pyplot as plt
import numpy as np
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
           





