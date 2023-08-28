size = int(input("Size: "))
moves = int(input("Moves: "))
x, y = input("Knight: ").split(",")
position = [int(x), int(y)]

chess_board = []

for i in range(size):
    chess_board.append(["."] * size)


def print_board(board):
    for row in board:
        print(" ".join(row))

def calculate_move(board, position, iterations):
    if iterations <= moves:
      if board[position[0]][position[1]] == "." or int(board[position[0]][position[1]]) > iterations:
          board[position[0]][position[1]] = str(iterations)
          # list of new positions relative to position to check
          new_positions = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]
          for new_position in new_positions:
              # check if new position is on the board
              if position[0] + new_position[0] >= 0 and position[0] + new_position[0] < size and position[1] + new_position[1] >= 0 and position[1] + new_position[1] < size:
                  calculate_move(board, [position[0] + new_position[0], position[1] + new_position[1]], iterations + 1)


calculate_move(chess_board, position, 0)

print_board(chess_board)
