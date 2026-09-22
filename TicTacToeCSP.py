# Tic-Tac-Toe using CSP and Backtracking


# CSP Variables
variables = list(range(9))


# CSP Domain
domain = ["X", "O", " "]


# Winning Constraints
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


# Display board
def show(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


# Check constraints
def winner(board):
    for a, b, c in winning_combinations:

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


# Check if board is full
def is_board_full(board):
    return " " not in board


# Check if move is valid
def is_valid_move(board, position):
    return 0 <= position < 9 and board[position] == " "


# CSP Backtracking
def find_move(board):

    # Try every position
    for position in variables:

        # Check if position is empty
        if is_valid_move(board, position):

            # Temporarily assign O
            board[position] = "O"

            # Check constraint
            if winner(board) == "O":

                # Undo temporary assignment
                board[position] = " "

                return position

            # Backtrack
            board[position] = " "

    return -1


# Main game
board = [" "] * 9


# Show position numbers
print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")


while True:

    # Display board
    show(board)


    # Human move
    p = int(input("Enter position (1-9): ")) - 1


    # Check valid move
    if not is_valid_move(board, p):
        print("Invalid move!")
        continue


    # Assign X
    board[p] = "X"


    # Check if human won
    if winner(board) == "X":
        break


    # Check draw
    if is_board_full(board):
        break


    # Computer move
    move = find_move(board)


    # If no winning move, choose any empty position
    if move == -1:

        for position in variables:

            if is_valid_move(board, position):
                move = position
                break


    # Assign O
    board[move] = "O"


    # Check if computer won
    if winner(board) == "O":
        break


# Final board
show(board)


# Final result
if winner(board) == "X":
    print("You Win!")

elif winner(board) == "O":
    print("Computer Wins!")

else:
    print("Draw!")