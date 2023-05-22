import random
import time

def generate_sequence(diff):
        list = []
        for n in range(diff):
          number = random.randrange(1, 101)
          list.append(number)
        while True:
            print(list, end='')
            time.sleep(0.7)
            print('', end='\r')
            break
        return list


def get_list_from_user(diff):
        guess_list = []
        for n in range (diff):
          guess= int(input())
          guess_list.append(guess)
        return guess_list


def is_list_equal(list,guess_list):
          if guess_list != list:
               print('Wrong! You Lost')
               equal = False
          else:
               print('godd job! You Win')
               equal = True
          return equal


def play(diff):
  print('Welcome to the Memory Game!!! Can you remember the ' + str(diff) + ' numbers That was flashing on the screen?')
  list = generate_sequence(diff)
  guess_list = get_list_from_user(diff)
  result = is_list_equal(list, guess_list)
  return result






