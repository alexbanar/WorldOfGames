from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from Utils import ERROR_MESSAGE
from Score import add_score

FIRST_GAME_NUM = 1
SECOND_GAME_NUM = 2
THIRD_GAME_NUM = 3
START_DIFFICULTY = 1
HIGHEST_DIFFICULTY = 5
player_name = ''
def welcome(name):
    global player_name
    player_name = name
    print("\nHello " + player_name +
          " and welcome to the World of Games (WoG).",
          "\nHere you can find many cool games to play.")

def load_game():
    global player_name
    while True:
        game_to_play_number_input = input("\nPlease choose a game to play: "\
                "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"\
                "\n2. Guess Game - guess a number and see if you choose like the computer"\
                "\n3. Exit"                          
                "\nEnter here: ")

        game_to_play_number = game_to_play_number_input.strip()
        if game_to_play_number.isdigit():
            game_to_play_number = int(game_to_play_number)
            if game_to_play_number == FIRST_GAME_NUM \
                    or game_to_play_number == SECOND_GAME_NUM\
                    or game_to_play_number == THIRD_GAME_NUM:
                break
            else:
                print('\n' + ERROR_MESSAGE)
        else:
            print('\n' + ERROR_MESSAGE)

    if game_to_play_number == THIRD_GAME_NUM:
        return

    difficulty_range = range(HIGHEST_DIFFICULTY)
    while True:
        game_difficulty_input = input("\nPlease choose game difficulty from 1 to 5: ")
        game_difficulty = game_difficulty_input.strip()
        if game_difficulty.isdigit():
            game_difficulty = int(game_difficulty)
            if (game_difficulty - 1) in difficulty_range:
                break
            else:
                print('\n' + ERROR_MESSAGE)
        else:
            print('\n' + ERROR_MESSAGE)

    if game_to_play_number == FIRST_GAME_NUM:

            is_player_win = play_memory_game(game_difficulty)
            while is_player_win == None:
                while True:
                    game_difficulty_input = input("\nPlease choose game difficulty from 1 to 5: ")
                    game_difficulty = game_difficulty_input.strip()
                    if game_difficulty.isdigit():
                        game_difficulty = int(game_difficulty)
                        if (game_difficulty - 1) in difficulty_range:
                            break
                        else:
                            print('\n' + ERROR_MESSAGE)
                    else:
                        print('\n' + ERROR_MESSAGE)

                is_player_win = play_memory_game(game_difficulty)

            if is_player_win == False:
                print('\n' + player_name + " - sorry, you lost the current game")
                load_game()
            else:
                print('\n' + player_name +
                      " - congratulations - you win the current game with " +
                str(game_difficulty) + " points!!!")

                add_score(game_difficulty)
                load_game()

    elif game_to_play_number == SECOND_GAME_NUM:
        is_player_win = play_guess_game(game_difficulty)
        if is_player_win == False:
            print('\n' + player_name + " - you lost the current game")
            load_game()
        else:
            print('\n' + player_name +
                  " - congratulations - you win the current game with " +
                  str(game_difficulty) + " points!!!")

            add_score(game_difficulty)
            load_game()

    else:
        None

