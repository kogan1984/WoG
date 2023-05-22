import random
def generate_number(diff):
        number = random.randint(1, diff)
        return number


def get_guess_from_user(diff):
        print('Welcome to the Guess Game!!! Can you guess the secret number? You got three attempts.')
        guess = input('Please guess a number between 1 and ' + str(diff) + ' :')
        guess=int(guess)
        return guess


def compare_results(number,guess):
          if guess != number:
            print('Wrong! You Lost.')
            win = False
          else:
            print('godd job! You Won.')
            win = True
          return win


def play(diff):
  number = generate_number(diff)
  guess = get_guess_from_user(diff)
  won = compare_results(number, guess)
  return won



