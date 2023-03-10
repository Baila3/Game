def matrixsolver():
  matrix = []
  rref = []
  rawNum1 = []
  rawNum2 = []
  rows = input("Number of rows: ")
  cols = input("Number of columns: ")
  x = 1
  y = 1
  z = 0
  w = 1
  mat = 1
  for entries in range(int(rows) * int(cols)):
    num = input('Enter number {0} for matrix 1: '.format(x))
    rawNum1.append(num)
    x+=1
  for entries in range(int(rows) * int(cols)):
    num = input('Enter number {0} for matrix 2: '.format(y))
    rawNum2.append(num)
    y+=1
    # row.append(num)

  matrix1 = [rawNum1[x:x+int(cols)] for x in range(0, len(rawNum1), int(cols))]
  matrix2 = [rawNum2[x:x+int(cols)] for x in range(0, len(rawNum2), int(cols))]
  # rref = [rawNum[x:x+int(cols)] for x in range(0, len(rawNum), int(cols))]