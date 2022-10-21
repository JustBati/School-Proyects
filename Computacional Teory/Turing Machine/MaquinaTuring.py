import random


#Definicion del la lista que almacene las opciones validas del lenguaje

lenguaje =["-","*","|","a","X"]
cadena=[]
memo = open("./Funcionamiento Turing.txt","w")

#-------------------------------------------------------------------------------
#----------------Descripcion de los estados-------------------------------------
#-------------------------------------------------------------------------------

"""
Primer estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "*"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""


def estado_1(cadena, id):
    if  (0<=id<len(cadena)):
        if(cadena[id]=="*"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ1(*)=XR2\tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ1(*)=XR2\tEn el indice: "+str(id)+"\n")
            cadena[id]="X"
            estado_2(cadena, id+1)
            

        else:
            cadena_not_ok()
    else:
        cadena_not_ok()

"""
Segundo estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "*" "|"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_2(cadena, id):
    
    if  (0<=id<len(cadena)):

        if(cadena[id]=="*"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ2(*)=R3\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ2(*)=R3\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_3(cadena,id+1)
            
        elif(cadena[id=="|"]):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ2(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ2(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_2(cadena,id+1)
        else:
            cadena_not_ok()
    else:
        cadena_not_ok()
    

"""
Tercer estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "*" "|"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_3(cadena, id):
    
    if  (0<=id<len(cadena)):

        if(cadena[id]=="*"):
        
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ3(*)=XL4\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ3(*)=XL4\tEn el indice: \tEn el indice: "+str(id)+"\n")
            cadena[id]="X"
            estado_4(cadena, id-1)

        elif(cadena[id=="|"]):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ3(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ3(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_3(cadena,id+1)
        else:
            cadena_not_ok()
    else:
        cadena_not_ok()

        
"""
Cuarto estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "*" "|" "X"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_4(cadena, id):
    
    if  (0<=id<len(cadena)):
        if(cadena[id]=="*"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ4(|)=L\tEn el indice: \tEn el indice: "+str(id)+"0<=id\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ4(|)=L\tEn el indice: \tEn el indice: "+str(id)+"0<=id\n")
            estado_4(cadena, id-1)
        
        elif(cadena[id=="|"]):
            
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ4(|)=aR5\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ4(|)=aR5\tEn el indice: \tEn el indice: "+str(id)+"\n")
            cadena[id]="a"
            estado_5(cadena,id+1)

        elif(cadena[id]=="X"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ4(X)=R7\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ4(X)=R7\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_7(cadena, id+1)
        else:
            cadena_not_ok()
    else:
        cadena_not_ok()
        
"""
Quinto estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "-" "*" "|" "X"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_5(cadena, id):
    
    if  (0<=id<len(cadena)):

    
        if(cadena[id]=="-"):
            
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(-)=|L6\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(-)=|L6\tEn el indice: \tEn el indice: "+str(id)+"\n")
            cadena[id]="|"
            estado_6(cadena, id-1)

        elif(cadena[id=="*"]):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(*)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(*)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_5(cadena,id+1)

        elif(cadena[id]=="|"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_5(cadena, id+1)

        elif(cadena[id]=="X"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(X)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ5(X)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_5(cadena,id+1)
        else:
            cadena_not_ok()
    else:
        cadena_not_ok()

        
"""
Sexto estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
         "*" "|" "a" "X"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_6(cadena, id):
    
    if  (0<=id<len(cadena)):

    
        if(cadena[id]=="*"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(*)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(*)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_6(cadena, id-1)

        elif(cadena[id=="|"]):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(|)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(|)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_6(cadena,id-1)

        elif(cadena[id]=="a"):
            
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(a)=|L4\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(a)=|L4\tEn el indice: \tEn el indice: "+str(id)+"\n")
            cadena[id]="|"
            estado_4(cadena, id-1)

        elif(cadena[id]=="X"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(X)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ6(X)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_6(cadena,id-1)
        else:
            cadena_not_ok()
    else:
        cadena_not_ok()


        
"""
Septimp estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "*" "|"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_7(cadena, id):
    
    if  (0<=id<len(cadena)):

        if(cadena[id]=="*"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ7(*)=R8\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ7(*)=R8\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_8(cadena, id+1)

        elif(cadena[id=="|"]):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ7(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ7(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_7(cadena,id+1)
        else:
            cadena_not_ok()


    else:
        cadena_not_ok()

    
        
"""
Octavo estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "-" "|" "X"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_8(cadena, id):
    
    if  (0<=id<len(cadena)):
        if(cadena[id]=="-"):  
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ8(-)=*L9\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ8(-)=*L9\tEn el indice: \tEn el indice: "+str(id)+"\n")
            cadena[id]="*"
            estado_9(cadena, id-1)

        elif(cadena[id=="|"]):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ8(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ8(|)=R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_8(cadena,id+1)
            
        elif(cadena[id]=="X"):
            
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ8(X)=*R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ8(X)=*R\tEn el indice: \tEn el indice: "+str(id)+"\n")
            cadena[id]="*"
            estado_8(cadena, id+1)
        else:
            cadena_not_ok()
    else:
        cadena_not_ok()

    
    
        
"""
Noveno estado de la maquina de turing:
    Funciona si y solo si ingresan los caracteres:
        "*" "|" "X"
    De entrar los demas caracteres la cadena
    no forma parte del lenguaje

    Recibe:
        Cadena a ser evaluada
        Id de la posicion del caracter a evaluar
    Regresa:
        Null
    Funcionamiento:
        En caso de existir una coincidencia de estado/caracter
        se avanzara al estado correspondiente y se haran las correcciones necesarias segun el caso
"""
def estado_9(cadena, id):
    
    if  (0<=id<len(cadena)):
        
        if(cadena[id]=="*"):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ9(*)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ9(*)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_9(cadena, id-1)
        elif(cadena[id=="|"]):
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ9(|)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ9(|)=L\tEn el indice: \tEn el indice: "+str(id)+"\n")
            estado_9(cadena,id-1)
        elif(cadena[id]=="X"):
            
            memo.write("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ9(X)=*!\tEn el indice: \tEn el indice: "+str(id)+"\n")
            print("\nCadena evaluada:\n"+"".join(cadena)+"\nRegla aplicada:\tQ9(X)=*!\tEn el indice: \tEn el indice: "+str(id)+"\n")
            cadena[id]="*"
            cadena_ok()
        else:
            cadena_not_ok()   
    else:
        cadena_not_ok()


#-------------------------------------------------------------------------------
#----------------Descripcion de Funciones---------------------------------------
#-------------------------------------------------------------------------------

def cadena_ok():
    print("cadena existente en el lenguaje")
    memo.write("\n\n\tCadena existente en el lenjuage")

def cadena_not_ok():
    print("cadena no existente en el lenguaje")
    memo.write("\n\n\tCadena no existente en el lenjuage")

def get_cadena():
    print("Ingrese la cadena de la forma:\n\t-,*,|,a,X,...")
    usua=input("\t-->")
    cadena=usua.split(",")
    estado_1(cadena,0)

def cadena_random():
    n=random.randint(0,50)
    for i in range(n):
        cadena.append("")
        cadena[i]=random.choice(lenguaje)
    print(f"{cadena}")
    estado_1(cadena,0)

#-------------------------------------------------------------------------------
#----------------Funcion Main---------------------------------------------------
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    sele=0
    while sele!=3:
        print("1- Insertar una cadena para ser examinada por la maquina de Turing")
        print("2- Generar una cadena aleatoriamente para ser examinada por la maquina de Turing")
        print("3- Salir")
        sele=int(input("--> "))
        if(sele==1):
            get_cadena()
        elif(sele==2):
            cadena_random()

    memo.close()