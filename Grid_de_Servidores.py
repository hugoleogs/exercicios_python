# PROBLEMA:
# Um grid de servidores está configurado para replicar arquivos entre si.
# Quando um servidor recebe um arquivo, ele transfere esse arquivo para
# os servidores adjacentes que não o possuem, levando 1 hora para tal. Dada
# uma configuraçâo de grid em certo momento, qual o tempo mínimo para que todo_
# o grid possua a cópia de um arquivo? Considere que a configuração seja
# representada por uma matriz binária M x N, contendo M linhas e N coluna,
# na qual o valor 0 represente que um servidor não possui o arquivo, e
# o valor 1 represente que o servidor possui o arquivo.

# INPUT:
# - rows = número de linhas do grid;
# - columns = número de colunas do grid;
# - grid = matriz (array de arrays) binária representando a configuração
# dos servidores.

# OUTPUT:
# quantidade mínima de horas para todo_ o grid possuir o mesmo arquivo.

## INPUT:
## rows = 5
## columns = 5
## grid = [[1, 0, 0, 0, 0],
##         [0, 1, 0, 0, 0],
##         [0, 0, 1, 0, 0],
##         [0, 0, 0, 1, 0],
##         [0, 0, 0, 0, 1]]

## OUTPUT:
## 4
horas = 0

def converte (rows, columns, grid):

    for i in range(rows):

        for j in range(columns):

            if grid[i][j] == 2:

                grid[i][j] = 1

    return 1


def minimumHours(rows, columns, grid):
    ## SEU CÓDIGO AQUI
    verifica = []

    for i in range(rows):

        for j in range(columns):

            if grid[i][j] == 1:

                if (i-1) >= 0 and grid[i-1][j] == 0:

                    grid[i-1][j] = 2
                    verifica.append(True)
                else:

                    verifica.append(False)

                if (i+1) <= rows-1 and grid[i+1][j] == 0:

                    grid[i+1][j] = 2
                    verifica.append(True)
                else:

                    verifica.append(False)

                if (j - 1) >= 0 and grid[i][j-1] == 0:

                    grid[i][j-1] = 2
                    verifica.append(True)
                else:

                    verifica.append(False)

                if (j + 1) <= columns - 1 and grid[i][j+1] == 0:

                    grid[i][j+1] = 2
                    verifica.append(True)
                else:

                    verifica.append(False)
    global horas
    horas = horas + converte(rows, columns, grid)

    if any(verifica):
        minimumHours(rows, columns, grid)



rows = 5
columns = 5
grid = [[1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]]

minimumHours(rows, columns, grid)

print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])

print(horas-1)