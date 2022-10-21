import random
import time
"""
-Funcion para generar una cadena aleatoria de 64 bits
#no recibe nada
#regresa una cadena aleatoria de 64 bits

"""
def Gene():
    x = format(random.randint(0, 2**64) ,"b")#pasa binario
    if (len(x)<64):#comprueba que la cadena tenga la cantidad deseada de bits
        for j in range(64-len(x) ):#agrega 0s en una cadena a concatenar
            c=''
            if (j == 0):
                    c = "0"
            else:
                c = c + "0"    
        
            x = c + x
    return x

"""
-Automata Finito Determinista de Paridad
Recibe : Una cadena 
Funcionamiento : Mediante estados y el id del estado determina la paridad de 0's y 1's en la cadena recibida
Regresa : El id del estado, donde el estado aceptado para paridad, o el estado final es el '0'
"""
def Paridad(cadena):
    q=0
    for j in cadena:
        #Primer nodo y estado final
        if(q==0 and j=='0'):
            q=2
        elif(q==0 and j=='0'):
            q=1
        #Segundo nodo
        elif(q==1 and j=='0'):
            q=2
        elif(q==1 and j=='1'):
            q=0
        #Tercer nodo
        elif(q==2 and j=='1'):
            q=2
        elif(q==2 and j=='0'):
            q=0
        #Cuarto nodo
        elif(q==2 and j=='1'):
            q=2
        elif(q==2 and j=='0'):
            q=0
    return q

"""
-Crea el archivo de informacion donde estaran las 10**6 cadenas de 64bits
"""
def Proto():
    flujo = open("Protocolo.txt","a")
    for i in range(100):    
        flujo.write(f"{Gene()}\n")

    flujo.close()
    print("\n\tEl archivo de cadenas  se ha creado correctamente\n")

"""
-Funcion para registrar la cadena en el archivo correcto segun sea el caso
Recibe : Cadena de 64 bits y estado resultante del automata de paridad
Regresa : null
"""
def guardar(cadena, estado):
    correcto = open("Acaptado.txt","a")
    rechazado= open("Rechazado.txt","a")    
    if(estado==0):
        correcto.write(f"{cadena} ")
    else:
        rechazado.write(f"{cadena}")
    correcto.close()
    rechazado.close()


"""
Funcion main
"""
n=1
sele=0
sele=random.getrandbits(1)
while sele==1:
    Proto()
    print(f"Corrida #{n} del protocolo")
    time.sleep(1)
    flujo = open("Protocolo.txt","r")
    for j in range(10**2): 
        cadena=flujo.readline()
        estado=Paridad(cadena)
        guardar(cadena, estado)
    sele=random.getrandbits(1)
    flujo.close()
    n+=1
if sele==0:
    print("\n\n\n\tEl protocolo no corrio")