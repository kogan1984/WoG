def welcome():
  name = input("Please Enter your name: ")
  print ("Hello " + name+ " and welcome to the World of Games (WoG).\n"
"Here you can find many cool games to play.\n")

def load_game():
       print ( """Please choose a game to play:
       1. Memory Game - a sequence of numbers will appear for 1 second and you have to
       guess it back
       2. Guess Game - guess a number and see if you chose like the computer
       3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
       choice = input('Please Select a game:')
       while not (choice.isdigit() and 1 <= int(choice) <= 3):
           choice = (input("Please enter only numbers between 1-3\n"
                 "try again..."))
       choice = int(choice)
       diff = input('Please choose game difficulty from 1 to 5:')
       while not (diff.isdigit() and 1 <= int(diff) <= 5):
           choice = (input("Please enter only numbers between 1-5\n"
                 "try again:"))
       diff = int(diff)
       if choice == 1:
           from MemoryGame import play
           play(diff)
       if choice == 2:
           from GuessGame import play
           play(diff)
       if choice == 3:
           from CurrencyRouletteGame import play
           play(diff)



