def rotateImage(image,direction):
  if direction != "left" and direction != "right":
    return "Enter either 'left' or 'right' exactly for rotation direction!"
  elif len(image) != len(image[0]):
    return "Image not a NxN matrix!" #Assumes No Jagged Array Entered
  elif len(image) == 1:
    return image    #Image entered is 1 element long, can't rotate.

  length = len(image) - 1 #length of array zeroindexed

  for i in range(len(image)/2):
    for j in range(i, length-i):
      top = image[i][j]
      right = image[j][length-i]
      bottom = image[length-i][length-j] 
      left = image[length-j][i]

      if direction == "right":
        image[j][length-i] = top
        image[length-i][length-j] = right
        image[length-j][i] = bottom
        image[i][j] = left
      elif direction == "left":
        image[j][length-i] = bottom
        image[length-i][length-j] = left
        image[length-j][i] = top
        image[i][j] = right

  return image


matrix1 = [[0 for x in range(5)] for x in range(5)]
matrix2 = [[0 for x in range(5)] for x in range(5)]
matrix3 = [[0 for x in range(1)] for x in range(1)]
matrix4 = [[0 for x in range(1)] for x in range(2)]
counter = 1
for i in range(5):
  for j in range(5):
    matrix1[i][j] = counter
    matrix2[i][j] = counter
    counter += 1

print matrix1
print rotateImage(matrix1, "left")
print rotateImage(matrix2, "right")
print rotateImage(matrix2, "left")
print rotateImage(matrix3, "left")
print rotateImage(matrix3, "asdf")
print rotateImage(matrix4, "left")
