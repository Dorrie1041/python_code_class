import random

did = False
count = int(input('Please enter a number that you like to play: \t'))


# determine player want to continue or not
def start_game(a):
    if a == 'Y':
        return True
    else:
        return False


answer = input('Enter Y to start new game, if N to end the game: \t')

while start_game(answer) and count > 0:
    guess = random.randint(1, 10)
    count -= 1
    # user can guess number for 3 times
    for i in range(3):
        n = int(input('Enter a number between 1 and 10: \t'))
        if n == guess:
            print("You got the number ")
            break
        elif n > guess:
            print("Too high")
        else:
            print("Too low")
    if count > 0:
        answer = input('Enter Y to start new game, if N to end the game: \t')
