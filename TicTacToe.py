def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]

    while True:
        print_board(board)

        while True:
            try:
                row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
                col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
                
                # Check if the entered row and column are within the valid range
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == ' ':
                        board[row][col] = current_player
                        break
                    else:
                        print("That cell is already taken. Try again.")
                else:
                    print("Invalid row or column. Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

if __name__ == "__main__":
    tic_tac_toe()
