import random

guessUpRange = 99
guessDownRange = 0

guess = random.randint(guessDownRange, guessUpRange)
print(guess, 'How is this? (d:equal, b:greater, k:smaller)')
state = input()

while state != 'd':
    if state == 'b':
        guessDownRange = guess
        guess = random.randint(guessDownRange, guessUpRange)
    elif state == 'k':
        guessUpRange = guess
        guess = random.randint(guessDownRange, guessUpRange)
    print(guess, 'How is this? (d:equal, b:greater, k:smaller)')
    state = input()

print('HAHA! I won! It was:', guess)