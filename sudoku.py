import numpy as np

def isSafe(grid, row, col, num):
    # Verifica se o número pode ser colocado na linha ou coluna sem violar as regras do Sudoku
    if num in grid[row, :] or num in grid[:, col]:
        return False

    # Verifica se o número pode ser colocado na sub-grade 3x3 sem violar as regras do Sudoku
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    if np.any(grid[startRow:startRow+3, startCol:startCol+3] == num):
        return False

    return True

def solveSudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:
                for num in range(1, 10):
                    if isSafe(grid, row, col, num):
                        grid[row, col] = num
                        if solveSudoku(grid):
                            return True
                        grid[row, col] = 0  # Faz o backtracking se a colocação atual for inválida
                return False  # Se nenhum número válido for encontrado para esta célula
    return True

def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")  # Adiciona uma linha vertical após cada sub-grid de 3x3
        print("")
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)  # Adiciona uma linha horizontal após cada sub-grid de 3x3

# Exemplo de uso - Com solução:
'''grid = np.array([
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
])'''

#Exemplo de uso - Sem solução
grid = np.array([ 
    [3, 6, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
])

if solveSudoku(grid):
    print("Solução encontrada para o grid de 9x9:")
    printGrid(grid)
else:
    print("Não existe solução")
