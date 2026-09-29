import random

def display_board(rows):
    print()

    for row in rows:
        for cell in row:
            print(cell, end=" ")
        print()
    print()

def player_input():
    while True:
        player1 = input("Player 1: Select X or O ").upper()

        if player1 not in ["X", "O"]:
            continue

        if player1 == "X":
            player2 = "O"

        else:
            player2 = "X"

        return player1, player2

def place_marker(board,marker,position):
    row = (position - 1) // 3
    column = (position - 1) % 3
    board[row][column] = marker

def win_check(board,mark):

    # rows
    for row in board:
        if (row[0] == mark and
                row[1] == mark and
                row[2] == mark):
            return True

    #columns
    for column in range(3):
        if (board[0][column] == mark and
            board[1][column] == mark and
            board[2][column] == mark):
            return True

    #diagonal
    if (board[0][0] == mark and
    board[1][1] == mark and
    board[2][2] == mark):
        return True

    if (board[0][2] == mark and
    board[1][1] == mark and
    board[2][0] == mark):
        return True
    return False


def turns():

    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board,position):
    row = (position - 1) // 3
    column = (position - 1) % 3

    return board[row][column] == " "

def full_check(board):

    for position in range(1,10):
        if space_check(board,position):
            return False
    return True

def player_choice(board):

    while True:
        position = int(input("Choose a position (1-9): "))
        if position not in range(1,10):
            print("Invalid input")
        elif not space_check(board,position):
            print("This position is taken")
        else:
            return position


def replay():
    answer = input("Do you want to play again? (Y/N): ").upper()
    if answer == "Y":
        return True
    else:
        return False

def start_game():
    while True:
        start = input("Start the game? (yes,no):\n ").lower()

        if start not in ["yes", "no"]:
            continue

        elif start == "yes":
            return True

        elif start == "no":
            return False

def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    player1, player2 = player_input()

    turn = turns()

    print(turn + " is first")

    game_on = True

    while game_on:
        if turn == "Player 1":
            display_board(board)

            print("Player 1's turn")

            position = player_choice(board)

            place_marker(board,player1,position)

            if win_check(board,player1):
                display_board(board)

                print("Player 1 wins!")

                game_on = False
            elif full_check(board):
                display_board(board)

                print("Tie")

                game_on = False

            else:
                turn = "Player 2"
        else:
            display_board(board)

            print("Player 2's turn")

            position = player_choice(board)

            place_marker(board,player2,position)

            if win_check(board,player2):
                display_board(board)

                print("Player 2 wins!")

                game_on = False
            elif full_check(board):
                display_board(board)

                print("Tie")

                game_on = False

            else:
                turn = "Player 1"



def main():
    while True:

        print("Welcome to Tic-Tac Toe!")
        print()

        if start_game():
            play_game()

            if not replay():
                print("Thank you for playing!")
                break
        else:
            print("Bye")
            break
main()
