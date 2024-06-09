import os
import platform

BOARD = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

used_numbers = []


def welcome():
    print("""
___ _ ____ ___ ____ ____ ___ ____ ____
 |  | |     |  |__| |     |  |  | |___
 |  | |___  |  |  | |___  |  |__| |___
 
    """)
    print("Welcome!")
    print("Let's start the game! The board is below.")


def clear_screen():
    if platform.system() == "Windows":
        print('\n' * 80)
    else:
        os.system('clear')


def print_board(board):
    count = 0
    for element in board:
        if count < 3:
            if count < 2:
                print(element + " |", end=" ")
            else:
                print(element + " ", end=" ")
            count += 1

        if count == 3:
            print("\n")
            count = 0


def player_input(player, symbol):
    try:
        while True:
            user_answer = int(input(f"Player {player}: "))
            if user_answer < 1 or user_answer > 9:
                print("The number must be between 1 and 9.")
                continue
            if user_answer in used_numbers:
                print("This number is already used. Try again")
                continue
            BOARD[user_answer - 1] = symbol
            used_numbers.append(user_answer)
            break
    except ValueError:
        print("Invalid Input. Please enter a number between 1 and 9.")


def check_winner(board, symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for win in winning_combinations:
        if all(board[i] == symbol for i in win):
            return True
    return False


def check_draw(board):
    return all(draw in ['x', 'o'] for draw in board)


def reset_game():
    global BOARD, used_numbers
    BOARD = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    used_numbers = []


game_on = True
while game_on:
    reset_game()
    welcome()
    print("Type number between 1 and 9!")
    current_player = 1
    game = True

    while game:
        print_board(BOARD)
        if current_player == 1:
            player_input(1, 'x')
            if check_winner(BOARD, 'x'):
                print_board(BOARD)
                print("Player 1 won!")
                game = False
            current_player = 2
        else:
            player_input(2, 'o')
            if check_winner(BOARD, 'o'):
                print_board(BOARD)
                print("Player 2 won!")
                game = False
            clear_screen()
            current_player = 1

        if check_draw(BOARD):
            print_board(BOARD)
            print("It's a draw!")
            game = False

    while True:
        play_again = input("Do you want to play again? Y/N: ").lower()
        if play_again in ['y', 'n']:
            break

    if play_again == 'n':
        game_on = False
        print("Thank for playing!")
