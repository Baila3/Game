def matrixsolver():
  matrix = []
  rref = []
  rawNum = []
  rows = input("Number of rows: ")
  cols = input("Number of columns: ")
  x = 1
  y = 0
  z = 0
  w = 1
  for entries in range(int(rows) * int(cols)):
    num = input('Enter number {0}: '.format(x))
    rawNum.append(num)
    x+=1
    # row.append(num)

  matrix = [rawNum[x:x+int(cols)] for x in range(0, len(rawNum), int(cols))]
  rref = [rawNum[x:x+int(cols)] for x in range(0, len(rawNum), int(cols))]
  
  for rows in range(len(matrix[0])):
    if matrix[y][y] != 1:
      rref[y][y] = int(matrix[y][y]) / int(matrix[y][y])

    if y + 1 != len(matrix):
      if matrix[y + 1][y] != 0:
        multiple = int(matrix[y + 1][y]) / int(matrix[y][y])
        rref[y + 1][y] = int(matrix[y + 1][y]) - (multiple * int(matrix[y][y]))
        y+=1
    else:
        multiple = int(matrix[y][y]) / int(matrix[0][0])
        rref[y][0] = int(matrix[y][y]) - (multiple * int(matrix[0][0]))

    if matrix[y][y] !=1:
      rref[y][y] = int(matrix[y][y]) / int(matrix[y][y])

    if matrix[y - 1][y] != 0:
      multiple = int(matrix[y - 1][y]) / int(matrix[1][1])
      rref[y - 1][y] = int(matrix[y - 1][y]) - (multiple * int(matrix[1][1]))
  print(matrix)
  print(rref)

matrixsolver()