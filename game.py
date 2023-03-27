VALID_INPUT = ["0", "1", "2"]

output_dict = {
    "InvalidMessage": "Invalid move. Please try again.",
    "SelectColumn": "Which column would you like to move? (0-2): ",
    "Tie": "It's a tie!"
    
}


def print_board(board):
    print("-------------")
    for i in range(3):
        print("| " + str(board[i*3]) + " | " +
              str(board[i*3+1]) + " | " + str(board[i*3+2]) + " |")
        print("-------------")


def check_win(board, player):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6))

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True

    return False

def tic_tac_toe():
    board = [" "] * 9
    player = "X"
    print_board(board)

    while True:
        row = input("It's your turn, " + player +
                    ". Which row would you like to move? (0-2): ")
        col = input(output_dict("SelectColumn"))
        try:
            row = int(row)
            col = int(col)
            move = row * 3 + col
            if row not in VALID_INPUT or col not in VALID_INPUT or board[move] != " ":
                print(output_dict["InvalidMessage"])
                continue
        except ValueError:
            print(output_dict["InvalidMessage"])
            continue

        board[move] = player
        print_board(board)

        if check_win(board, player):
            print(player + " wins!")
            break
        elif all([True if cell != " " else False for cell in board]):
            print(output_dict["Tie"])
            break

        player = "O" if player == "X" else "X"


tic_tac_toe(True)
