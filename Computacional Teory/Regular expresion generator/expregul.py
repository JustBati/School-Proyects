import random
#Listas en las cuales se guardaran las cadenas resultantes, y las elecciones de
#la expresion regular
cuerpo=["0","01"]
cerradura=["e","0","1"]
exp=[]

#Archivo donde se guarda el proceso de la expresion
memo = open("./Impresiones.txt","w")

"""
Funcion donde se genera de manera aleatoria una cadena dentro del lenguaje de la expresion regular
Recibe:
        Indice de la expresion regular que se esta trabajando
"""

def generador(i):
    n=random.randint(0,10)
    print(f"Expresion {i+1}")
    memo.write("Expresion\t"+str(i+1)+"\n")
    exp.append("")
    for j in range(n):
        val= random.choice(cuerpo)
        print(f"{i}=\t{exp[i]} + {val}")
        memo.write(str(i)+" =\t" + exp[i]+" + "+val+"\n")
        exp[i]= exp[i] + val
    for k in range(1000):
        val=random.choice(cerradura)
        memo.write(str(i)+" =\t" + exp[i]+" + "+val+"\n")
        if val=="e":
            print(f"Expresion {i} terminada\t{exp[i]}\n")
            memo.write("Expresion "+str(i)+" terminada \n\t"+exp[i]+"\n\n")
            break
        else:
            exp[i]= exp[i]+ val
            print(f"{i}=\t{exp[i]} + {val}")

if __name__ == '__main__':       
    for i in range(10):
        generador(i)
    memo.close()