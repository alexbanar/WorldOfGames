from Live import load_game, welcome
from Utils import ERROR_MESSAGE
from Utils import screen_cleaner

def get_player_name():
    player_name = ''
    while True:
        player_name_input = input("Please enter your name: ")
        player_name = player_name_input.strip()
        if player_name.isalpha():
            break
        else:
            print('\n' + ERROR_MESSAGE)

    proper_player_name = ''
    for i in range(len(player_name)):
        if i == 0:
            proper_player_name += player_name[0].capitalize()
        else:
            proper_player_name += player_name[i].lower()
    return proper_player_name

screen_cleaner()
welcome(get_player_name())
load_game()