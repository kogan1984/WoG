import Utils
def add_score(diff):
    POINTS_OF_WINNING = (diff*3)+5
    try:
        with open(Utils.SCORES_FILE_NAME, 'r+') as f:
            number = f.readline()
            sum = int(number)+POINTS_OF_WINNING
            f.seek(0)
            f.write(str(sum))
    except ValueError:
        with open(Utils.SCORES_FILE_NAME, 'w+') as f:
            f.write(str(POINTS_OF_WINNING))
    except FileNotFoundError:
        with open(Utils.SCORES_FILE_NAME, 'w+') as f:
            f.write(str(POINTS_OF_WINNING))

