# INCOMPLETE

def board_is_happy(board):
  is_happy = True
  # each thing can be accessed as board[y][x]

  size = len(board) # square size

  for i in range(size):
    for j in range(size):
      if board[i][j] == 'L':
        # check if there is a lightbulb in the same row or column.
        for k in range(size):
          if board[i][k] == 'L' or board[k][j] == 'L':
            is_happy = False
            break
  return is_happy  # TODO


def board_is_solved(board):
  return False  # TODO


def get_board_state(board):
  if board_is_happy(board):
    if board_is_solved(board):
      return 'solved'
    else:
      return 'happy'
  else:
    return 'unhappy'


if __name__ == '__main__':
  # Example board, happy state.
  print(get_board_state('''
...1.0.
X......
..X.X..
X...L.X
..X.3..
.L....X
L3L2...'''.strip().split('\n')))
  # Example board, solved state.
  print(get_board_state('''
..L1.0.
X...L..
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Example board, unhappy state.
  print(get_board_state('''
L..1L0.
X.L....
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Different board, happy state.
  print(get_board_state('''
L1.L.
..L3L
..X1.
.1...
.....'''.strip().split('\n')))