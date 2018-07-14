def checkCrossword(grid):
    for row in range(len(grid)):
        rowDiff = grid[row][1] - grid[row][0]
        for col in range(2,len(grid[0])):
            if grid[row][col] - grid[row][col-1] != rowDiff:
                return False
    for col in range(len(grid[0])):
        colDiff = grid[1][col] - grid[0][col]
        for row in range(2,len(grid)):
            if grid[row][col] - grid[row-1][col] != colDiff:
                return False
    return True

def findEmpty(grid):
    for row in grid:
        for col in row:
            if col == -1:
                return True
    return False

def solveCrossword(grid):
    
    while findEmpty(grid):
        #solve any rows that have at least 2 entries
        for row in range(len(grid)):
            count = 0
            elements = []
            for col in range(len(grid[0])):
                if grid[row][col] != -1:
                    count += 1
                    elements.append(col)
            if count > 1:
                solveRow(grid,row,elements)
        #solve any cols that have at least 2 entries
        for col in range(len(grid[0])):
            count = 0
            elements = []
            for row in range(len(grid)):
                if grid[row][col] != -1:
                    count += 1
                    elements.append(row)
            if count > 1:
                solveCol(grid,col,elements)
        #solve remaining grid
    for row in grid:
        print(*row,sep='\t')

def solveRow(grid,row,elements):
    spaceBetween = elements[1] - elements[0]
    diff = (grid[row][elements[1]] - grid[row][elements[0]]) / spaceBetween
    start = grid[row][elements[0]] - elements[0]*spaceBetween
    for col in range(len(grid[0])):
        grid[row][col] = int(start + diff*col)
    
def solveCol(grid,col,elements):
    spaceBetween = elements[1] - elements[0]
    diff = (grid[elements[1]][col] - grid[elements[0]][col]) / spaceBetween
    start = grid[elements[0]][col] - elements[0]*spaceBetween
    for row in range(len(grid)):
        grid[row][col] = int(start + diff*row)   
    

basicSolved = [[23, 28, 33],
              [19, 18, 17],
              [15, 8, 1]]

basicIncorrect = [[23, 28, 33],
                  [19, 18, 17],
                  [16, 8, 1]]

basicPossible = [[23, 28, -1],
                [19, -1, -1],
                [-1, -1, 1]]

basicPossible2 = [[23, -1, 33],
                  [-1, -1, -1],
                  [15, -1, 1]]

print(checkCrossword(basicSolved))
print(checkCrossword(basicIncorrect))

print(solveCrossword(basicPossible))
print(solveCrossword(basicPossible2))
