def esta_sudoku_armado(sudoku):
    # Verificar filas
    for i in range(9):
        #Verifica si cada fila tiene 9 elementos distintos, si no tiene 9 entonces retorna false
        if len(set(sudoku[i])) != 9: 
            return False

    # Verificar columnas
    for i in range(9):
        #Verifica si cada columna tiene 9 elementos distintos, si no tiene 9 entonces retorna false
        if len(set([sudoku[j][i] for j in range(9)])) != 9:
            return False

    # Verificar cuadrantes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cuadrante = []
            #Arma los cuadrantes
            for x in range(3):
                for y in range(3):
                    cuadrante.append(sudoku[i+x][j+y])
            #Verifica si el cuadrante tiene 9 elementos distintos, si no tiene 9 entonces retorna false
            if len(set(cuadrante)) != 9:
                return False

    return True


sudoku_no_armado = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,0,1,0,9,5],
          [0,0,7,0,8,0,1,0,0]]

print("Esta armado" if esta_sudoku_armado(sudoku_no_armado) else "No esta armado")

sudoku_armado = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]

print("Esta armado" if esta_sudoku_armado(sudoku_armado) else "No esta armado")
