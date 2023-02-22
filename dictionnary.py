def matrixsolver():
  matrix = []
  row = []
  rawNum = []
  rows = input("Number of rows: ")
  cols = input("Number of columns: ")
  x = 1
  for entries in range(int(rows) * int(cols)):
    num = input('Enter number {0}: '.format(x))
    rawNum.append(num)
    x+=1
    row.append(num)
  matrix = [rawNum[x:x+int(cols)] for x in range(0, len(rawNum), int(cols))]

    # if len(row) > int(cols):
    #   for entry in range(int(cols)):
    #     matrix.append(row)  
  # i = 0
  # while i < int(rows):
  #   matrix.append([])
  #   i+= 1
  print(matrix)
  # print(matrix)

matrixsolver()