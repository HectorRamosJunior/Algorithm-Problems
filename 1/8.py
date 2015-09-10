"""
  Write an algorithm such that if an element in a MxN matrix is 0, 
  its entire row and column are set to 0.
"""


def zeroMatrix(matrix):
  #Assumes no Jagged Arrays

  #Function places 0 in first row/col of respective row/col
  #To Call back later to remove 0's.
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        matrix[0][j] = 0
        matrix[i][0] = 0

  for i in range(1, len(matrix)): #Rows to 0
    if matrix[i][0] == 0:
      for j in range(1, len(matrix[0])):
        matrix[i][j] = 0

  for i in range(1, len(matrix[0])): #Cols to 0
    if matrix[0][i] == 0:
      for j in range(1, len(matrix)):
        matrix[j][i] = 0

  #If the first element is 0, has to be done last
  #Otherwise all rows and columns would be set to zero during the above loops
  if matrix[0][0] == 0: 
    for i in range(len(matrix)): 
        matrix[i][0] = 0
    for j in range(len(matrix[0])): 
        matrix[0][j] = 0

  return matrix


matrix1 = [[x for x in range(5)] for x in range(7)]
matrix2 = [[x+1 for x in range(5)] for x in range(7)]

print matrix1
print zeroMatrix(matrix1)
print matrix2
print zeroMatrix(matrix2)

matrix2[2][4] = 0
matrix2[0][1] = 0
print matrix2
print zeroMatrix(matrix2)
