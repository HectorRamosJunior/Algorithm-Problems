"""
  Write an algorithm such that if an element in a MxN matrix is 0, 
  its entire row and column are set to 0.
"""

def zeroMatrix(m):
    matrix = [x[:] for x in m]


    zeroRow = set()
    zeroCol = set()

    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[0])):
            if matrix[row][col] == 0:
                if not row in zeroRow:
                    zeroRow.add(row)
                if not col in zeroCol:
                    zeroCol.add(col)

    for row in zeroRow:
        for col in xrange(len(matrix[0])):
            matrix[row][col] = 0

    for col in zeroCol:
        for row in xrange(len(matrix)):
            matrix[row][col] = 0

    return matrix

def zeroMatrix2(m):
    matrix = [x[:] for x in m]

    firstRow = False
    firstCol = False

    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[0])):
            if matrix[row][col] == 0:
                if row == 0:
                    firstCol = True
                if col == 0:
                    firstRow = True
                if row > 0:
                    matrix[row][0] = 0
                if col > 0:
                    matrix[0][col] = 0

    for row in xrange(1, len(matrix)):
        if matrix[row][0] == 0:
            for col in xrange(1, len(matrix[0])):
                matrix[row][col] = 0

    for col in xrange(1, len(matrix[0])):
        if matrix[0][col] == 0:
            for row in xrange(1, len(matrix)):
                matrix[row][col] = 0


    if firstRow:
        for x in xrange(len(matrix[0])):
            matrix[0][x] = 0

    if firstCol:
        for x in xrange(len(matrix)):
            matrix[x][0] = 0

    return matrix

def printMatrix(matrix):
    print 
    for x in matrix:
        print x

matrix = [[1 for x in xrange(5)] for y in xrange(7)]

matrix[0][0] = 0
matrix[6][4] = 0
matrix[3][2] = 0

printMatrix(matrix)

printMatrix(zeroMatrix(matrix))
printMatrix(zeroMatrix2(matrix))

matrix1 = [0 for x in xrange(5)]
matrix2 = [[0 for x in xrange(5)]]

printMatrix(matrix1)
printMatrix(matrix2)

printMatrix(zeroMatrix(matrix1))
printMatrix(zeroMatrix2(matrix2))
