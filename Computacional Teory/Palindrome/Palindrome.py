import random
memo=open("./Funcionamiento.txt","w")

#Reglas para la generacion del palindromo 
cerrar = ["0","1"]
cuerpo=["0P0","1P1"]
def generar(n,pal_izq,pal_der,pal):
    pal="P"

    inpar=n%2
    print(f"El largo del palindromo es: {n}")
    print(f"\t\t{pal_izq+ pal +pal_der}")
    memo.write("\nEl largo del palindromo es: "+str(n)+"\n"+"\t\t"+pal_izq+pal+pal_der+"\n")
    for i in range(int(n/2)):
        op=random.choice(cuerpo)
        
        if(op=="0P0"):
            pal_izq=pal_izq+"0"
            pal_der="0"+pal_der
            print(f"P -> 0P0\t-->\t{pal_izq+ pal +pal_der}")
            memo.write("P -> 0P0\t-->\t"+pal_izq+pal+pal_der+"\n")
        elif(op=="1P1"):
            pal_izq=pal_izq+"1"
            pal_der="1"+pal_der
            print(f"P -> 1P1\t-->\t{pal_izq+ pal +pal_der}")
            memo.write("P -> 1P1\t-->\t"+pal_izq+pal+pal_der+"\n")
    terminar(inpar, pal_izq,pal_der,pal)
    

def terminar(inpar,pal_izq,pal_der,pal):
    
    if (inpar==0):
        pal="e"
        print(f"P -> e\t-->\t{pal_izq +pal_der}")
        memo.write("P -> e\t-->\t"+pal_izq+pal_der+"\n")
    elif(inpar==1):
        pal=random.choice(cerrar)
        print(f"P -> {pal}-->\t{pal_izq+ pal +pal_der}")
        memo.write("P -> "+pal+"-->\t"+pal_izq+pal+pal_der+"\n")

if __name__ == '__main__':
    sele=""
    while (sele!=3):
        print("1- Insertar un numero para la generacion del paindrome")
        print("2- Generar un palindrome aleatoriamente de hasta 100K caracteres")
        print("3- Salir")
        sele=int(input("--> "))
        if(sele==1):
            n=int(input("\n\t-->"))
            generar(n,"","","")
        elif(sele==2):
            generar(random.randint(0,1000),"","","")



    memo.close()
