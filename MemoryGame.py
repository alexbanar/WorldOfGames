import random
from Utils import screen_cleaner, freeze_screen
from Utils import ERROR_MESSAGE

START_RANDOM = 1
END_RANDOM = 101
FREEZE_SCREEN_TIME_SEQ_FLOAT = 0.7

# The list will be shown for 0.7 seconds (using Utils.py module).
def generate_sequence(difficulty):
    random_numbers_list = []
    for i in range(difficulty):
        result_generated_number = random.randint(START_RANDOM, END_RANDOM)
        # random_numbers_list.insert(len(random_numbers_list), result_generated_number)
        random_numbers_list.append(result_generated_number)

    print("\nComputer generated sequence is:")
    for element in random_numbers_list:
        print(element, end=' ')

    # wait("freeze" the screen) FREEZE_SCREEN_TIME_SEQ_FLOAT(0.7) seconds
    # to see computer generated numbers sequence and continue
    # after that with printing of user explanation header
    # for continuation of the Memory Game
    freeze_screen(FREEZE_SCREEN_TIME_SEQ_FLOAT)

    return random_numbers_list

def print_memory_game_header():
    print("After seeing the numbers, enter the numbers you saw," \
          "\neach one separated with Enter:")

def get_list_from_user(difficulty):
    user_numbers_list = []
    # print("\nAfter seeing the numbers, enter the numbers you saw,"\
    #       "\neach one separated with Enter:")

    for i in range(difficulty):
        while True:
            curr_input_number_input = input()
            curr_input_number = curr_input_number_input.strip()
            if curr_input_number.isdigit():
                curr_input_number = int(curr_input_number)
                break
            else:
                print('\n' + ERROR_MESSAGE)
                return None
                # print("You have inserted " + str(i) +
                #       " numbers from " + str(difficulty) + " until now" +
                #       "\nPlease continue..")

        # user_numbers_list.insert(len(user_numbers_list), curr_input_number)
        user_numbers_list.append(curr_input_number)

    return user_numbers_list

def is_list_equal(list_a, list_b):
    return set(list_a) == set(list_b)

def play(difficulty):
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    if list_b == None:
        return None
    is_player_win = is_list_equal(list_a, list_b)
    return is_player_win
