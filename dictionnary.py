def matrixsolver():
  matrix = []
  rows = input("Number of rows: ")
  cols = input("Number of columns: ")
  x = 1
  for entries in range(int(rows) * int(cols)):
      num = input('Enter number {0}: '.format(x))
      matrix.append(num)
      x+=1
  # i = 0
  # while i < int(rows):
  #   matrix.append([])
  #   i+= 1
  print(matrix)

matrixsolver()