"""
  Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
  write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotateMatrix(m, rotation):
    if len(m) <= 1:
        return m

    matrix = [row[:] for row in m]

    length = len(matrix) - 1

    for layer in xrange(len(matrix)/2):
        for step in xrange(length - layer * 2):
            topLeft = matrix[layer][step + layer]
            topRight = matrix[step + layer][length - layer]
            bottomRight = matrix[length - layer][length - layer - step]
            bottomLeft =  matrix[length - layer - step][layer]

            if rotation == "left":
                matrix[layer][step + layer] = topRight
                matrix[step + layer][length - layer] = bottomRight
                matrix[length - layer][length - layer - step] = bottomLeft
                matrix[length - layer - step][layer] = topLeft

            elif rotation == "right":
                matrix[layer][step + layer] = bottomLeft
                matrix[step + layer][length - layer] = topLeft
                matrix[length - layer][length - layer - step] = topRight
                matrix[length - layer - step][layer] = bottomRight

    return matrix


counter = 0
matrix = [[counter + x for y in xrange(5)] for x in xrange(5)]
for x in xrange(len(matrix)):
    print matrix[x]


m = rotateMatrix(matrix, "left")
for x in xrange(len(m)):
    print m[x]

m = rotateMatrix(matrix, "right")
for x in xrange(len(m)):
    print m[x]