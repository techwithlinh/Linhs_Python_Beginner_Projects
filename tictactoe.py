def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def make_move(player, row, col, board):
    board[row][col] = player
    return board

def check_win(player, board):
    # check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # check columns
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return False
    return True

def get_move(player, board):
    print(f"It's player {player}'s turn.")
    row = int(input("Choose a row (0, 1, or 2): "))
    col = int(input("Choose a column (0, 1, or 2): "))

    if board[row][col] != "-":
        print("Invalid move. That spot is already taken. Try again.")
        return get_move(player, board)

    return row, col

def game():
    board = [["-" for j in range(3)] for i in range(3)]
    print_board(board)

    player = "X"
    while True:
        row, col = get_move(player, board)
        board = make_move(player, row, col, board)
        print_board(board)

        if check_win(player, board):
            print(f"Player {player} wins!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

game()
