import random as rd

def generarMatriz(fila, columna):
    matriz=[]

    for i in range(fila):
        valor=[]
        for j in range(columna):
            valor.append(0)
        matriz.append(valor)
    return matriz

def mostrarMatriz(matriz):
    for fil in matriz:
        print(fil)
    print()
    
def posicionAleatoria(matriz,fila,columna):
    # print(aux)
    pos_fl=rd.randrange(0,fila,1)
    pos_cl=rd.randrange(0,columna,1)
    
    pos_matriz=[0,0]
    pos_matriz[0]=pos_fl  # Fila aleatoria
    pos_matriz[1]=pos_cl  # Columna aleatoria
    
    return pos_matriz
    #print(pos_matriz)

if __name__ == "__main__":
    fila=int(input("Filas: "))
    columna=int(input("Columnas: "))
    estado=True
    
    while(estado):
        if fila>0 and columna>0:
            aux=generarMatriz(fila, columna)
            estado=False
        else:
            print("\nLos valores dados no son válidos. Intente nuevamente.")
            fila=int(input("Filas: "))
            columna=int(input("Columnas: "))
    
    print("\nLa matriz inicial es: \n")
    mostrarMatriz(aux)

    ejecucion=int(input("Número de repeticiones: "))

    for i in range(ejecucion):
        cambio=posicionAleatoria(aux,fila,columna)
        aux[cambio[0]][cambio[1]]=1
        
        print(f"Posición semi aleatoria: [{cambio[0]}][{cambio[1]}]")
        mostrarMatriz(aux)
        aux=generarMatriz(fila, columna)