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