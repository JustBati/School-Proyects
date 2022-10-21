import random
import time

def Gene():
    p2 =open("Protocolo.txt","a")
    
    for i in range (5):
        x = format(random.randint(0, 8) ,"b")#pasa binario
        if (len(x)<64):#comprueba que la cadena tenga la cantidad deseada de bits
            for j in range(4-len(x) ):#agrega 0s en una cadena a concatenar
                c=''
                if (j == 0):
                     c = "0"
                else:
                    c = c + "0"    
        
                x = c + x
        p2.write(f"{x}\n")
    p2.close()
    return 0

def Paridad():
    p2= open("Protocolo.txt", "r")
    p3=open("Aceptado.txt", "a")
    p4=open("Rechazado.txt", "a")
    q='0'
    for i in p2:
        xz=p2.readline()
        print(xz)
           
        if(q=='0'):
         p3.write(f'{xz} ')
        elif(not q=='0'):
         p4.write(f"{xz} ")
        q='0'
    p3.close()
    p4.close()
    p2.close()
    

def Protocolo():   
    conf= Gene()
    
    #if(conf == 0):
    #    print("El flujo de informacion ah sido creado\n")
    #else:
   #     print("No se ha podido crear el flujo")

    time.sleep(1)
    Paridad()
    
   # print("El protocolo ha concluido con exito")

yep=1
u=0
if (yep==0):
   # print("El protocolo no pudo correr.")
   aasdf="uwu"
elif(yep==1):
    
        Protocolo()
        yep= random.getrandbits(1)
        u+=1
        #print(f"\nEl protocolo corrio {u} veces")
       # print("\n-----------------------\n\n")   