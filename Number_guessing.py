import random as r

print("Welcome to Number Guess Game")
Guest = input('do you want to play Number Guessing game (Y/N) : ').lower()

while True:

    if ('y' not in Guest) and ('n' not in Guest) and (Guest != True):
        Guest = input('Invalid keyword\nType again : ').lower()

    elif 'y' in Guest:
        correct_number = r.randint(1, 25)
        guessed_number = int(input('\nYou have 3 guesses.\nGuess any number between 1 and 25\nGuess the number : '))
        tries = 1

        while True:

            if correct_number == guessed_number:
                print(f'Congrats you have guessed the correct number in {tries} times.')
                break

            elif tries == 3:
                print(f'Sorry Your guessed number is wrong. The number is {correct_number}.')
                break

            else:
                print(f'You have {3 - tries} guesses left.')
                tries += 1
                guessed_number = int(input('Guess again : '))

        Guest = input(f' do you want to play more (Y/N) : ')

    else:
        print(f'\nOk Bye. See You soon.')
        break