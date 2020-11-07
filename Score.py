from Utils import SCORES_FILE_NAME

def add_score(last_game_points):
    score_file = ''
    total_score = '0'
    new_total_score = 0
    try:
        score_file = open(SCORES_FILE_NAME, 'r')
        curr_total_score = score_file.read()
        if curr_total_score.isdigit():
            curr_total_score = int(curr_total_score)
            new_total_score = curr_total_score + last_game_points
        else:
            new_total_score = last_game_points
    except FileNotFoundError:
        total_score = last_game_points
    except IOError:
        None
    finally:
        if score_file != '':
            try:
                score_file.close()
            except IOError:
                None

    score_file = ''
    try:
        score_file = open(SCORES_FILE_NAME, 'w')
        score_file.write(str(new_total_score))

        print("Your current score is", new_total_score)
    except IOError:
        None
    finally:
        if score_file != '':
            try:
                score_file.close()
            except IOError:
                None

