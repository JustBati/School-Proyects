import random

posibilidades = []
ganadoras = []
rmov = {
    1:"2,5",
    2:"5,7",
    3:"2,4,7",
    4:"7",
    5:"2,10",
    6:"2,5,7,10",
    7:"2,4,10,12",
    8:"4,7,12",
    9:"5,10,13",
    10:"5,7,13,15",
    11:"7,10,12,15",
    12:"7,15",
    13:"10",
    14:"10,13,15",
    15:"10,12",
    16:"12,15"
}

bmov = {
    1:"6",
    2:"1,3,6",
    3:"6,8",
    4:"3,8",
    5:"1,6,9",
    6:"1,3,9,11",
    7:"3,6,8,11",
    8:"3,11",
    9:"6,14",
    10:"6,9,11,14",
    11:"6,8,14,16",
    12:"8,11,16",
    13:"9,14",
    14:"9,11",
    15:"11,14,16",
    16:"11"
}
"""
Funcion para emular el automata finito no determinista
Recibe: cadena de movimientos a realizar, la cantidad de movimientos hechos
hasta el momento, la posicion actual de la pieza y la posible jugada que es generada
Regresa: null
"""
def nfa(cad_mov, mov_hechos, posicion, jugada):
    mov_pos = []
    
    if mov_hechos < len(cad_mov):
        if cad_mov[mov_hechos] =="r":
            mov_pos = rmov[posicion].split(",")
           
        elif cad_mov[mov_hechos] =="b":
            mov_pos = bmov[posicion].split(",")
           
        for i in mov_pos:
            next_mov_pos = jugada + ","+ str(i)

            if i =="16":
                
                posibilidades.append(next_mov_pos)
                ganadoras.append(next_mov_pos)
            else:
                nfa(cad_mov, mov_hechos +1, int(i), next_mov_pos)
    elif mov_hechos == len(cad_mov):
        posibilidades.append(jugada)

"""
Funcion para generar una cadena de movimientos aleatoria con un largo
de entre 1 mov hasta 100
Recibe: null
Regresa: cadena de movimientos
"""

def gene_ale():
    movale = random.randint(1,10)
    cad_mov = ""
    for i in range(movale):
        j = random.randint(0,1)

        if j== 0:
            memo="r"
        else:
            memo="b"
        cad_mov = cad_mov + memo
        if (i< movale-1):
            cad_mov = cad_mov + ","
        else:
            print("\n"+cad_mov)
            return cad_mov

"""
Funcion para iniciar el NFA y guardar las jugadas resultantes
Recibe: cadenda de movimientos
Regresa: null
"""

def correr(cadena):
    print("\n\n\t Iniciando NFA")
    memo = cadena.split(",")
    nfa(memo,0,1,"1")
    fpos = open("Posibilidades.txt","w")
    fgan =open("Ganadoras.txt","w")

    for jugadas in posibilidades:
        fpos.write(jugadas+"\n")
    
    for gjugadas in ganadoras:
        fgan.write(gjugadas+"\n")
    
    fpos.close()
    fgan.close()

    print("\n\tJugadas calculadas y guardadas en sus archivos correspondientes\n\n")


"""
Funcion main
"""
if __name__ == '__main__':

    op=0
    while op!=3:

        posibilidades.clear()
        ganadoras.clear(    )
        print("1.-Ejecutar nfa con cadena aleatoria de longitud en el rango de 0-100")
        print("2.-Ejecutar nfa con cadena ingresada por usuario\n3.-Salir")
        op=int(input("\nElija la opcion deseada-->"))
        if op==1:
            correr(gene_ale())
        elif op==2:
            print("Introduzca cadena de tipo, con un maximo de 20 mov\n\tr,b,r,b,b,r")
            print("r=red\nb=black")
            cad_gen = input("-->")
            correr(cad_gen)

