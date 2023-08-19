def display_top(num_matrix, width):
  for i in range(width):
    num_matrix[0][i + 1] = '-'
  return num_matrix

def display_middle(num_matrix, width):
  for i in range(width):
    num_matrix[width + 1][i + 1] = '-'
  return num_matrix

def display_bottom(num_matrix, width):
  for i in range(width):
    num_matrix[2*width + 2][i + 1] = '-'
  return num_matrix

def display_top_left(num_matrix, width):
  for i in range(width):
    num_matrix[i + 1][0] = '|'
  return num_matrix

def display_bottom_left(num_matrix, width):
  for i in range(width):
    num_matrix[i + width + 2][0] = '|'
  return num_matrix

def display_top_right(num_matrix, width):
  for i in range(width):
    num_matrix[i + 1][width + 1] = '|'
  return num_matrix

def display_bottom_right(num_matrix, width):
  for i in range(width):
    num_matrix[i + width + 2][width + 1] = '|'
  return num_matrix

def print_matrix(num_matrix):
  for row in num_matrix:
    print(''.join(row))

def concat_matrices(matrices):
  result = []
  for i in range(len(matrices[0])):
    result.append([])
    for j in range(len(matrices)):
      result[i].extend(matrices[j][i])
      result[i].append(" ")

  # cut off spaces at the end of each row
  for i in range(len(result)):
    result[i] = result[i][:-1]
  
  return result

def number(num, width):
  num_rows = 2*width + 3
  num_cols = width + 2
  num_matrix = [[' ' for i in range(num_cols)] for j in range(num_rows)]

  if num == 0:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_bottom(num_matrix, width)
    num_matrix = display_top_left(num_matrix, width)
    num_matrix = display_bottom_left(num_matrix, width)
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 1:
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 2:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_middle(num_matrix, width)
    num_matrix = display_bottom(num_matrix, width)
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_left(num_matrix, width)
  elif num == 3:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_middle(num_matrix, width)
    num_matrix = display_bottom(num_matrix, width)
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 4:
    num_matrix = display_middle(num_matrix, width)
    num_matrix = display_top_left(num_matrix, width)
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 5:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_middle(num_matrix, width)
    num_matrix = display_bottom(num_matrix, width)
    num_matrix = display_top_left(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 6:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_middle(num_matrix, width)
    num_matrix = display_bottom(num_matrix, width)
    num_matrix = display_top_left(num_matrix, width)
    num_matrix = display_bottom_left(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 7:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 8:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_middle(num_matrix, width)
    num_matrix = display_bottom(num_matrix, width)
    num_matrix = display_top_left(num_matrix, width)
    num_matrix = display_bottom_left(num_matrix, width)
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
  elif num == 9:
    num_matrix = display_top(num_matrix, width)
    num_matrix = display_middle(num_matrix, width)
    num_matrix = display_top_left(num_matrix, width)
    num_matrix = display_top_right(num_matrix, width)
    num_matrix = display_bottom_right(num_matrix, width)
    num_matrix = display_bottom(num_matrix, width)

  return num_matrix

number_to_display = input("Number: ")
width = int(input("Width: "))
numbers = []

for num in number_to_display:
  numbers.append(number(int(num), width))

print_matrix(concat_matrices(numbers))