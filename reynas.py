#Funcion que indica si el vector tiene mas de un 1 (1 = reyna)
def contiene_duplicados(vector):
    #print(lista)
    contador = 0
    for casilla in vector:
        if casilla == 1:
            contador = contador + 1
    if contador > 1:
        return True
    
#Funcion que determina si hay reinas atacandose de manera diagonal (superior derecha)
def valida_superior_derecha(lst): #LISTO
    for i in range(8):
        vector = []
        fila = 0
        columna = i
        for j in range(8 - columna):
            #print(fila, columna)
            vector.append(lst[fila][columna])
            columna = columna + 1
            fila = fila + 1
        if(contiene_duplicados(vector)):
            return True

#Funcion que determina si hay reinas atacandose de manera diagonal (superior izquierda)
def valida_superior_izquierda(lst):
    for i in range(8):
        vector = []
        fila = 7 - i
        columna = 0
        for j in range(fila + 1 - columna):
            #print(fila, columna)
            vector.append(lst[fila][columna])
            columna = columna + 1
            fila = fila - 1
        if(contiene_duplicados(vector)):
            return True

#Funcion que determina si hay reinas atacandose de manera diagonal (inferior derecha)    
def valida_inferior_derecha(lst): #LISTO
    for i in range(8):
        vector = []
        fila = 7
        columna = i
        for j in range(8 - columna):
            #print(fila, columna)
            vector.append(lst[fila][columna])
            columna = columna + 1
            fila = fila - 1
        if(contiene_duplicados(vector)):
            return True

#Funcion que determina si hay reinas atacandose de manera diagonal (inferior izquierda)
def valida_inferior_izquierda(lst): #LISTO
    for i in range(8):
        vector = []
        fila = 0
        columna = i
        for j in range(8 - columna):
            #print(columna, fila)
            vector.append(lst[columna][fila])
            columna = columna + 1
            fila = fila + 1
        if(contiene_duplicados(vector)):
            return True
        
def evaluar_cuadrantes(reynas):
    if (valida_superior_derecha(reynas)):
        return True
    if (valida_superior_izquierda(reynas)):
        return True
    
    return (valida_superior_derecha(reynas) or 
            valida_superior_izquierda(reynas) or 
            valida_inferior_derecha(reynas) or 
            valida_inferior_izquierda(reynas))


def reynas_atacando(reynas):
    # Primer caso donde hay mas de una reyna en la fila, por ende se estan atacando
    for i in range(8):
        #1.1  Se valida la fila
        if (contiene_duplicados(reynas[i])):
            return True
    
    # Segundo caso donde hay mas de una reyna en la columna, por ende se estan atacando
    # 2.1 Se prepara la columna
    for i in range(0, 8):
        columna = []
        for j in range(0, 8):
            columna.append(reynas[j][i])
        #print(columna)
        #2.2 Se valida la columna
        if (contiene_duplicados(columna)):
            return True
        
    # Tercer caso donde hay mas de una reyna en sus diagonales
    return evaluar_cuadrantes(reynas)


reynas_guerra = [
    [1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0]]

print("Estan atacando" if reynas_atacando(reynas_guerra) else "No estan atacando")


reynas_paz = [
    [1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0]]

print("Estan atacando" if reynas_atacando(reynas_paz) else "No estan atacando")


