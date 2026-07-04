# Tic-Tac-Toe AI

# Create an empty board
board = [' ' for _ in range(9)]


# Function to print the board
def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


# Function to check winner
def check_winner(player):
    winning_combinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


# Function to check draw
def check_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# Find the Best Move
def best_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


print("Welcome to Tic-Tac-Toe!")

while True:

    print_board()

    # Player Move
    while True:
        position = int(input("Enter a position (1-9): "))

        if position < 1 or position > 9:
            print("Invalid Position! Try Again.")

        elif board[position-1] != " ":
            print("Position Already Occupied!")

        else:
            board[position-1] = "X"
            break

    # Check Player Win
    if check_winner("X"):
        print_board()
        print("🎉 Congratulations! You Win!")
        break

    # Check Draw
    if check_draw():
        print_board()
        print("It's a Draw!")
        break

    # Computer Move
    best_move()
    
    print("\nComputer's Move:")

    # Check Computer Win
    if check_winner("O"):
        print_board()
        print("🤖 Computer Wins!")
        break

    # Check Draw
    if check_draw():
        print_board()
        print("It's a Draw!")
        break