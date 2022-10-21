import random

def automata(cadena):
    pila=["z0"]
    descri = open("./Funcionamiento.txt","w")
    print("\n\n------------------------\n\n")
    for estado in cadena:
        if(estado=="0"):
            pila.append("x")
            print("se añade un x a la pila, se detecto un 0")
            descri.write("se añade un x a la pila, se detecto un 0\n")
        elif(estado=="1"):
            if(len(pila)>=1):
                pila.pop()
                print("se elimina un iten de la pila, se detecto un 1")
                descri.write("se elimina un iten de la pila, se detecto un 1\n")
            else:
                print("cadena no aceptada por el automata")
                descri.write("cadena no aceptada por el automata\n")
                descri.close()
                return 0
             
    if(len(pila)==1):
        print("cadena aceptada ")
        descri.write("cadena aceptada por el automata\n")
        descri.close()
                
        return 1  
    else:
        print("cadena no aceptada por el automata ")
        descri.write("cadena no aceptada por el automata\n")
        descri.close()
                
        return 0

    
def aleatoria():
    cadena=""
    n = random.randint(0,100000)
    for i in range(n):
        cadena= cadena +str(random.randint(0,1))

    return cadena


if __name__ == '__main__':
    op=0
    while op!=3:
        print("\n\n------------------------\n\n")
        print("1.-Ejecutar automata pila con cadena aleatoria de longitud en el rango de 0-100,000")
        print("2.-Ejecutar automata pila con cadena ingresada por usuario\n3.-Salir")
        op=int(input("\nElija la opcion deseada-->"))

        if(op==1):
            automata(aleatoria())
        elif(op==2):
            n=input("-->")
            
            automata(n)
