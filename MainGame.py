from Live import load_game, welcome
welcome()
play = 'y'
while  play == 'y':
    load_game()
    play = input('Do You want To play again y/n:')
    if play == 'n':
        break


