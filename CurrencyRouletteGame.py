import requests
from datetime import date
import random
from py_currency_converter import convert


def get_money_interval(diff,random_USD):
    ILS_Value = convert(base='USD', amount=random_USD, to=['ILS'])['ILS']
    interval = ((ILS_Value - (5 - diff)), (ILS_Value + (5 - diff)))
    return interval


def get_guess_from_user(diff,random_USD):
   guess = input('Please guess the equivalent of '+str(random_USD)+ ' USD in ILS: ')
   return guess


def play(diff):
    random_USD = random.randrange(1, 100)
    interval = get_money_interval(diff, random_USD)
    guess = get_guess_from_user(diff, random_USD)
    if interval[0]< int(guess) <interval[1]:
        print('print good job! You nailed it!!!')
        won = True
    else:
        print('Wrong Buddy! better luck next time...')
        won = False
    return won
