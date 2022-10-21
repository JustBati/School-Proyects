
#-------------------------------------------------------------------------------
#----------------Descripcion de los estados-------------------------------------
#-------------------------------------------------------------------------------

""""
Estado 1
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_1(caracter):
    if (caracter=="w"):
        imprimir(caracter,1,12)
        return 12
        
    elif(caracter=="e"):
        imprimir(caracter,1,123)
        return 123
    elif(caracter=="c"):
        
        imprimir(caracter,1,127)
        return 127
    else:
        imprimir(caracter,1,1)
        return 1
    

""""
Estado 12
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_12(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,12,12)
        return 12
        
    elif(caracter=="e"):
        
        imprimir(caracter,12,1233)
        return 1233
    elif(caracter=="c"):
        
        imprimir(caracter,12,127)
        return 127
    else:
        
        imprimir(caracter,12,1)
        return 1

""""
Estado 123
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_123(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,123,12)
        return 12
        
    elif(caracter=="e"):
        
        imprimir(caracter,123,123)
        return 123
    elif(caracter=="b"):
        
        imprimir(caracter,123,124)
        return 124
    elif(caracter=="c"):
        
        imprimir(caracter,123,127)
        return 127
    else:
        
        imprimir(caracter,123,1)
        return 1
    

""""
Estado 127
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_127(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,127,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,127,123)
        return 123
    elif(caracter=="o"):
        
        imprimir(caracter,127,128)
        return 128
    elif(caracter=="c"):
        
        imprimir(caracter,127,127)
        return 127
    else:
        
        imprimir(caracter,127,1)
        return 1

""""
Estado 1233
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
        Id de la posicion del caracter
        # de palabras encontradas
    Regresa:
        Null
"""
def estado_1233(caracter, id_word,nword):
    if (caracter=="w"):
        
        imprimir(caracter,1233,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,1233,123)
        return 123
    elif(caracter=="b"):#estado final de web
        
        imprimir(caracter,1233,1244)
        print(f"Palabra 'web' en la posicion {id_word}")
        memo.write(f"Palabra 'web' en la posicion {id_word}\n")
        nword=nword+1
        return 1244
    elif(caracter=="c"):
        imprimir(caracter,1233,127)
        return 127
    else:
        
        imprimir(caracter,1233,1)
        return 1    

""""
Estado 124
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_124(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,124,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,124,123)
        return 123
    elif(caracter=="a"):
        
        imprimir(caracter,124,125)
        return 125
    elif(caracter=="c"):
        
        imprimir(caracter,124,127)
        return 127
    else:
        
        imprimir(caracter,124,1)
        return 1

""""
Estado 128
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_128(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,128,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,128,123)
        return 123
    elif(caracter=="i"):
        
        imprimir(caracter,128,129)
        return 129
    elif(caracter=="c"):
        
        imprimir(caracter,128,127)
        return 127
    else:
        
        imprimir(caracter,128,1)
        return 1

""""
Estado 1244
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_1244(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,1244,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,1244,123)
        return 123
    elif(caracter=="p"):
        
        imprimir(caracter,1244,15)
        return 15
    elif(caracter=="a"):
        
        imprimir(caracter,1244,125)
        return 125
    elif(caracter=="s"):
        
        imprimir(caracter,1244,19)
        return 19
    elif(caracter=="m"):
        
        imprimir(caracter,1244,113)
        return 113
    elif(caracter=="h"):
        
        imprimir(caracter,1244,119)
        return 119
    elif(caracter=="c"):
        
        imprimir(caracter,1244,127)
        return 127
    else:
        
        imprimir(caracter,1244,1)
        return 1

""""
Estado 125
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
        Id de la posicion del caracter
        # de palabras encontradas
    Regresa:
        Null
"""
def estado_125(caracter, id_word, nword):
    if (caracter=="w"):
        
        imprimir(caracter,125,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,125,123)
        return 123
    elif(caracter=="y"):
        
        imprimir(caracter,125,126)
        print(f"Palabra 'ebay' en la posicion {id_word}")#estado final de ebay
        memo.write(f"Palabra 'ebay' en la posicion {id_word}\n")
        nword=nword+1
        return 126
    elif(caracter=="c"):
        
        imprimir(caracter,125,127)
        return 127
    else:
        
        imprimir(caracter,125,1)
        return 1
""""
Estado 129
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
        Id de la posicion del caracter
        # de palabras encontradas
    Regresa:
        Null
"""
def estado_129(caracter, id_word,nword):
    if (caracter=="w"):
        
        imprimir(caracter,129,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,129,123)
        return 123
    elif(caracter=="n"):
        
        imprimir(caracter,129,130)
        print(f"Palabra 'coin' en la posicion {id_word}")#estado final de coin
        memo.write(f"Palabra 'coin' en la posicion {id_word}\n")
        nword=nword+1
        return 130
    elif(caracter=="c"):
        
        imprimir(caracter,129,127)
        return 127
    else:
        
        imprimir(caracter,129,1)
        return 1

""""
Estado 15
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_15(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,15,12)
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,15,123)
        return 123
    elif(caracter=="a"):
        
        imprimir(caracter,15,16)
        return 16
    elif(caracter=="c"):
        
        imprimir(caracter,15,127)
        return 127
    else:
        
        imprimir(caracter,15,1)
        return 1
""""
Estado 19
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_19(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,19,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,19,123)
        return 123
    elif(caracter=="i"):
        
        imprimir(caracter,19,110)
        return 110
    elif(caracter=="c"):
        
        imprimir(caracter,19,127)
        return 127
    else:
        
        imprimir(caracter,19,1)
        return 1

""""
Estado 113
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_113(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,113,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,113,123)
        return 123
    elif(caracter=="a"):
        
        imprimir(caracter,113,114)
        return 114
    elif(caracter=="c"):
        
        imprimir(caracter,113,127)
        return 127
    else:
        
        imprimir(caracter,113,1)
        return 1

""""
Estado 119
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_119(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,119,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,119,123)
        return 123
    elif(caracter=="o"):
        
        imprimir(caracter,119,120)
        return 120
    elif(caracter=="c"):
        
        imprimir(caracter,119,127)
        return 127
    else:
        
        imprimir(caracter,119,1)
        return 1

""""
Estado 126
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_126(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,126,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,126,123)
        return 123
    elif(caracter=="c"):
        
        imprimir(caracter,126,127)
        return 127
    else:
        
        imprimir(caracter,126,1)
        return 1

""""
Estado 130
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_130(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,130,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,130,123)
        return 123
    elif(caracter=="c"):
        
        imprimir(caracter,130,127)
        return 127
    else:
        
        imprimir(caracter,130,1)
        return 1

""""
Estado 16
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_16(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,16,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,16,123)
        return 123
    elif(caracter=="g"):
        
        imprimir(caracter,16,17)
        return 17
    elif(caracter=="c"):
        
        imprimir(caracter,16,127)
        return 127
    else:
        
        imprimir(caracter,126,1)
        return 1

""""
Estado 110
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_110(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,110,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,110,123)
        return 123
    elif(caracter=="t"):
        
        imprimir(caracter,110,111)
        return 111
    elif(caracter=="c"):
        
        imprimir(caracter,110,127)
        return 127
    else:
        
        imprimir(caracter,126,1)
        return 1

""""
Estado 114
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_114(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,114,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,114,123)
        return 123
    elif(caracter=="s"):
        
        imprimir(caracter,114,115)
        return 115
    elif(caracter=="c"):
        
        imprimir(caracter,114,127)
        return 127
    else:
        
        imprimir(caracter,114,1)
        return 1

""""
Estado 17
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
        Id de la posicion del caracter
        # de palabras encontradas
    Regresa:
        Null
"""
def estado_17(caracter,id_word,nword):
    if (caracter=="w"):
        
        imprimir(caracter,17,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,17,1238)
        print(f"Palabra 'webpage' en la posicion {id_word}")#estado final de webpage
        memo.write(f"Palabra 'webpage' en la posicion {id_word}\n")
        nword=nword+1
        return 1238
    elif(caracter=="c"):
        
        imprimir(caracter,17,127)
        return 127
    else:
        
        imprimir(caracter,17,1)
        return 1


""""
Estado 111
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
        Id de la posicion del caracter
        # de palabras encontradas
    Regresa:
        Null
"""
def estado_111(caracter,id_word,nword):
    if (caracter=="w"):
        
        imprimir(caracter,111,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,111,12312)
        print(f"Palabra 'website' en la posicion {id_word}")#estado final de website
        memo.write(f"Palabra 'website' en la posicion {id_word}\n")
        nword=nword+1
        return 12312
    elif(caracter=="c"):
        
        imprimir(caracter,111,127)
        return 127
    else:
        
        imprimir(caracter,111,1)
        return 1

""""
Estado 115
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_115(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,115,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,115,123)
        return 123
    elif(caracter=="t"):
        
        imprimir(caracter,115,116)
        return 116
    elif(caracter=="c"):
        
        imprimir(caracter,115,127)
        return 127
    else:
        
        imprimir(caracter,115,1)
        return 1


""""
Estado 1238
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_1238(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,1238,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,1238,123)
        return 123
    elif(caracter=="c"):
        
        imprimir(caracter,1238,127)
        return 127
    else:
        
        imprimir(caracter,1238,1)
        return 1

""""
Estado 12312
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_12312(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,12312,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,12312,123)
        return 123
    elif(caracter=="c"):
        
        imprimir(caracter,12312,127)
        return 127
    else:
        
        imprimir(caracter,12312,1)
        return 1

""""
Estado 120
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_120(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,120,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,120,123)
        return 123
    elif(caracter=="m"):
        
        imprimir(caracter,120,121)
        return 121
    elif(caracter=="c"):
        
        imprimir(caracter,120,127)
        return 127
    else:
        
        imprimir(caracter,120,1)
        return 1

""""
Estado 116
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_116(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,116,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,116,12317)
        return 12317
    elif(caracter=="c"):
        
        imprimir(caracter,116,127)
        return 127
    else:
        
        imprimir(caracter,116,1)
        return 1

""""
Estado 121
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
        Id de la posicion del caracter
        # de palabras encontradas
    Regresa:
        Null
"""
def estado_121(caracter,id_word,nword):
    if (caracter=="w"):
        
        imprimir(caracter,121,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,121,12322)
        print(f"Palabra 'webhome' en la posicion {id_word}")#estado final de webhome
        memo.write(f"Palabra 'webhome' en la posicion {id_word}\n")
        nword=nword+1
        return 12322
    elif(caracter=="c"):
        
        imprimir(caracter,121,127)
        return 127
    else:
        
        imprimir(caracter,121,1)
        return 1

""""
Estado 12317
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
        Id de la posicion del caracter
        # de palabras encontradas
    Regresa:
        Null
"""
def estado_12317(caracter,id_word,nword):
    if (caracter=="w"):
        
        imprimir(caracter,12317,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,12317,123)
        return 123
    elif(caracter=="r"):
        
        imprimir(caracter,12317,118)
        print(f"Palabra 'webmaster' en la posicion {id_word}")#estado final de webmaster
        memo.write(f"Palabra 'webmaster' en la posicion {id_word}\n")
        nword=nword+1
        return 118
    elif(caracter=="c"):
        
        imprimir(caracter,12317,127)
        return 127
    else:
        
        imprimir(caracter,12317,1)
        return 1


""""
Estado 12322
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_12322(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,12322,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,12322,123)
        return 123
    elif(caracter=="c"):
        
        imprimir(caracter,12322,127)
        return 127
    else:
        
        imprimir(caracter,12322,1)
        return 1

""""
Estado 118
    Recibe:
        Id del estado actual
        Caracter a ser evaluado
    Regresa:
        Null
"""
def estado_118(caracter):
    if (caracter=="w"):
        
        imprimir(caracter,118,12)   
        return 12
    elif(caracter=="e"):
        
        imprimir(caracter,118,123)
        return 123
    elif(caracter=="c"):
        
        imprimir(caracter,118,127)
        return 127
    else:
        
        imprimir(caracter,118,1)
        return 1

#-------------------------------------------------------------------------------
#----------------Descripcion de funciones---------------------------------------------------
#-------------------------------------------------------------------------------

def imprimir(caracter, id_ini, id_fin):
    print(f"q{id_ini}({caracter})->q{id_fin}")
    memo.write(f"q{id_ini}({caracter}) -> q{id_fin}\n")

def automata(cadena):
    lista=list(cadena)
    id=1
    nword=0
    i=0
    for caracter in lista:
        i=i+1 
        if (id==1):#1
            id=estado_1(caracter)
        elif(id==12):#2
            id=estado_12(caracter)
        elif(id==123):#3
            id=estado_123(caracter)
        elif(id==127):#4
            id=estado_127(caracter)
        elif(id==1233):#5
            id=estado_1233(caracter,i,nword)
        elif(id==124):#6
            id=estado_124(caracter)
        elif(id==128):#7
            id=estado_128(caracter)
        elif(id==1244):#8
            id=estado_1244(caracter)
        elif(id==125):#9
            id=estado_125(caracter,i,nword)
        elif(id==129):#10
            id=estado_129(caracter,i,nword)
        elif(id==15):#11
            id=estado_15(caracter)
        elif(id==19):#12
            id=estado_19(caracter)
        elif(id==113):#13
            id=estado_113(caracter)
        elif(id==119):#14
            id=estado_119(caracter)
        elif(id==126):#15
            id=estado_126(caracter)
        elif(id==130):#16
            id=estado_130(caracter)
        elif(id==16):#17
            id=estado_16(caracter)
        elif(id==110):#18
            id=estado_110(caracter)
        elif(id==114):#19
            id=estado_114(caracter)
        elif(id==17):#20
            id=estado_17(caracter)
        elif(id==111):#21
            id=estado_111(caracter)
        elif(id==115):#22
            id=estado_115(caracter)
        elif(id==1238):#23
            id=estado_1238(caracter)
        elif(id==12312):#24
            id=estado_12312(caracter)
        elif(id==120):#25
            id=estado_120(caracter)
        elif(id==116):#26
            id=estado_116(caracter)
        elif(id==121):#27
            id=estado_121(caracter,i, nword)
        elif(id==12317):#28
            id=estado_12317(caracter,i,nword)
        elif(id==12322):#29
            id=estado_12322(caracter)
        elif(id==118):#30
            id=estado_118(caracter)
        else:
            print("ERROR")
        
        
#-------------------------------------------------------------------------------
#----------------Funcion Main---------------------------------------------------
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    sele=""
    while (sele!=3):
        print("1- Insertar una cadena a evaluar")
        print("2- Leer un archivo de texto")
        print("3- Salir")
        sele=int(input("--> "))
        if(sele==1):
            memo=open("Buscador de palabras.txt","w")
            c=input("\n\t-->")
            automata(c)
            memo.close()
        elif(sele==2):
            nombre=input("Nombre del archivo:\t")
            memo1=open(f"{nombre}","r")
            automata(memo1.readline())
            memo.close()
    
    