"""
  Write an algorithm such that if an element in a MxN matrix is 0, 
  its entire row and column are set to 0.
"""

#Creates two hash sets for the columns and rows with a 0
#Then iterates through and sets those to 0 at the end. 
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


#Sets the first row and column to 0 only, requires extra data structure
#However at the end this requires that the first row or column
#Is set to be all 0's after every other element is set
def zeroMatrix2(m):
    matrix = [x[:] for x in m]

    #Placeholders if the first row and column are
    #To be set to all 0 at the very end
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

    #Iterates through the first row/col looking to set the entire
    #Row or column to 0 if a 0 is found.
    #Ignores element [0][0] when iterating, would set all to 0
    for row in xrange(1, len(matrix)):
        if matrix[row][0] == 0:
            for col in xrange(1, len(matrix[0])):
                matrix[row][col] = 0

    for col in xrange(1, len(matrix[0])):
        if matrix[0][col] == 0:
            for row in xrange(1, len(matrix)):
                matrix[row][col] = 0


    #Set first row/col to 0 if called for
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

matrix1 = [[x+1 for x in xrange(5)]]
matrix1[0][3] = 0

printMatrix(matrix1)

printMatrix(zeroMatrix(matrix1))

