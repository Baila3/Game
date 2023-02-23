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
  if matrix[0][0] != 1:
   for numbers in range(len(matrix[0])):
    rref[0][y] = int(matrix[0][y]) / int(matrix[0][0])
    y+=1

  if matrix[1][0] != 0:
   multiple = int(matrix[1][0]) / int(matrix[0][0])
   for numbers in range(len(matrix[1])):
    rref[1][z] = int(matrix[1][z]) - (multiple * int(matrix[0][z]))
    z+=1

  if matrix[1][1] !=1:
    rref[1][1] = int(matrix[1][1]) / int(matrix[1][1])

  if matrix[0][1] != 0:
   multiple = int(matrix[0][1]) / int(matrix[1][1])
   rref[0][1] = int(matrix[0][1]) - (multiple * int(matrix[1][1]))

  print(matrix)
  print(rref)

matrixsolver()