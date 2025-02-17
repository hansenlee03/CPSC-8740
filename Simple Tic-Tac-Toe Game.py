def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"
    moves = 0
    
    while True:
        display_board(board)
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            if choice < 0 or choice > 8 or board[choice] != " ":
                print("Invalid move. Try again.")
                continue
            board[choice] = current_player
            moves += 1
            
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif moves == 9:
                display_board(board)
                print("It's a tie!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Please enter a valid number.")

tic_tac_toe()
