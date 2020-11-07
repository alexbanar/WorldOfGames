import random
from Utils import ERROR_MESSAGE

START_DIFFICULTY = 1

def generate_number(difficulty):
    result_generated_number = random.randint(START_DIFFICULTY, difficulty)
    # print(result_generated_number)
    return result_generated_number


def get_guess_from_user(difficulty):
    user_chosen_difficulty_range = range(difficulty)
    while True:
        user_guessed_number_input = input("Please guess a number between " +
                                    str(START_DIFFICULTY) + " to " + str(difficulty) + ' : ')
        user_guessed_number = user_guessed_number_input.strip()
        if user_guessed_number.isdigit():
            user_guessed_number = int(user_guessed_number)
            if (user_guessed_number - 1) in user_chosen_difficulty_range:
                break
            else:
                print('\n' + ERROR_MESSAGE)
        else:
            print('\n' + ERROR_MESSAGE)

    return user_guessed_number

def compare_results(difficulty, secret_number):
    user_guessed_difficulty = get_guess_from_user(difficulty)
    if secret_number == user_guessed_difficulty:
        return True
    else:
        return False

def play(difficulty):
    secret_number = generate_number(difficulty)
    is_player_win = compare_results(difficulty, secret_number)
    return is_player_win
